import json
import sys
import os

# Добавляем текущую директорию в путь Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SITE.settings')

import django
django.setup()

from django.core import serializers

# ИМЕНА ТВОИХ ПРИЛОЖЕНИЙ И МОДЕЛЕЙ
APP_NAME = 'main'  # имя папки с models.py
MODEL_NAMES = ['Math', 'Physics', 'Informatics']  # имена моделей

print(f"Экспортируем данные из приложения: {APP_NAME}")  # ← исправлено: APP_NAME

all_data = []

for model_name in MODEL_NAMES:
    try:
        # Импортируем модель
        model = __import__(f'{APP_NAME}.models', fromlist=[model_name])  # ← исправлено: APP_NAME
        ModelClass = getattr(model, model_name)

        # Получаем данные
        objects = ModelClass.objects.all()
        data = serializers.serialize('json', objects, ensure_ascii=False, indent=2)

        all_data.extend(json.loads(data))
        print(f"✓ {model_name}: {objects.count()} записей")

    except Exception as e:
        print(f"✗ Ошибка в {model_name}: {e}")

# Сохраняем в файл
if all_data:
    with open('my_data.json', 'w', encoding='utf-8') as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Данные сохранены в my_data.json")
    print(f"   Всего записей: {len(all_data)}")
else:
    print("\n❌ Не удалось экспортировать данные")