from rest_framework import serializers
from itertools import groupby
import re


default_error_messages = {
    'blank': 'این فیلد الزامی است'
}

class NameSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, error_messages=default_error_messages)

    def validate_name(self, value):
        name = value
        msg_check_name = []                
        persian_pattern = r'^[آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی ]+$'
        

        if len(name) < 3 :
            msg_check_name.append('طول فیلد باید بیشتر از ۳ کاراکتر باشد')
        if len(name) > 100:
            msg_check_name.append('طول فیلد باید کمتر از ۱۰۰ کاراکتر باشد')
        if len(max(name.split(), key=len)) > 14:
            msg_check_name.append('طول هر کلمه نباید بیشتر از ۱۴ حرف باشد')
        if name.count(" ") > 5:
            msg_check_name.append('بیشتر از 5 فاصله غیرقابل قبول است')
        if not bool(re.match(persian_pattern, name)):
            msg_check_name.append('تنها حروف زبان فارسی پذیرفته میشود')
        if not msg_check_name:
            return value
        
        raise serializers.ValidationError(msg_check_name)


class CellSerializer(serializers.Serializer):
    cell = serializers.CharField(required=True, error_messages=default_error_messages)

    def validate_cell(self, value):
        cell = value
        msg_check_cell = [] 
        number_pattern = r'[0-9]+$'
        list_code = ['0911', '0921', '0912', '0935', '0936']
        groups = groupby(cell)
        consecutive_counts = [sum(1 for _ in group) for label, group in groups]
        
        if len(cell) != 11:
            msg_check_cell.append('شماره تلفن باید یازده رقم باشد')
        if ' ' in cell:
            msg_check_cell.append('فصله قابل پذیرش نیست')
        if cell[0] != '0':
            msg_check_cell.append('شماره موبایل باید با صفر شروع شود')
        if not bool(re.match(number_pattern, cell)):
            msg_check_cell.append('شماره تلفن فقط عددد باشد')
        if not cell[:4] in list_code:
            msg_check_cell.append("پیش شماره های مجاز '0911', '0921', '0912', '0935', '0936'")
        if 6 in consecutive_counts:
            msg_check_cell.append('هیچ رقمی در شماره موبایل نباید بیش از پنج بار پشت سرهم تکرار شده باشد')
        if not msg_check_cell:
            return value
        
        raise serializers.ValidationError(msg_check_cell)


class RoadSerializer(serializers.Serializer):
    road = serializers.CharField(required=True, error_messages=default_error_messages)

    def validate_road(self, value):
        road = value
        msg_check_road = []
        list_word_filter = ['بالاتر از', 'بعد از', 'نرسیده به', 'قبل از', 'روبروی', 'مقابل']
        if 50 < len(road) or len(road) < 2:
            msg_check_road.append('لطفا تعداد حروف مابین ۲ تا ۵۰ حرف باشد')
        if len(re.split('[" " , _]',road)) > 5:
            msg_check_road.append('بیشتر از ۵ کلمه مجاز نیست عبارات جدا کننده شامل فاصله ـ , می باشد')
        if len(max(re.split('[" " , _]', road), key=len)) > 14:
            msg_check_road.append('هر کلمه نباید بیشتر از ۱۴ کاراکتر باشد')
        if any(word in road for word in list_word_filter):
            msg_check_road.append("مسیر نباید شامل هیچ یک از کلمات 'بالاتر از', 'بعد از', 'نرسیده به', 'قبل از', 'روبروی', 'مقابل' باشد")
        if not msg_check_road:
            return value
        
        raise serializers.ValidationError(msg_check_road)


class HouseNumberSerializer(serializers.Serializer):
    house_number = serializers.CharField(required=True, error_messages=default_error_messages)

    def validate_house_number(self, value):
        house_number = value
        msg_check_house_number = []
        illegal_pattern = r'.*[@#\$%\^\&\*\(\)].*'
        two_char_pattern = r'.*[آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی\s]+[آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی\s].*'

        if 5 < len(house_number) or len(house_number) < 1:
            msg_check_house_number.append('لطفا تعداد حروف مابین ۱ تا ۵ حرف باشد')
        if bool(re.match(illegal_pattern, house_number)):
            msg_check_house_number.append('کاراکترهای@#$%^&*() غیرمجاز است')
        if bool(re.match(two_char_pattern, house_number)):
            msg_check_house_number.append('دو حرف فارسی پشت سرهم قابل قبول نیست')
        if not msg_check_house_number:
            return value
        
        raise serializers.ValidationError(msg_check_house_number)
