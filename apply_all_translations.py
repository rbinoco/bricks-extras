#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete Translation Applier for BricksExtras fa_IR.po file
Applies all professional Persian translations to the .po file
"""

import re
import sys

# Import the complete translation dictionary
sys.path.insert(0, '.')

# Comprehensive translation dictionary (manually curated professional translations)
translations_dict = {
    # Already translated in previous script - base translations
    "%s Conditions": "%s شرایط",
    "(touch devices)": "(دستگاه های لمسی)",
    "1 month": "1 ماه",
    "1 year": "1 سال",

    # New comprehensive translations for remaining strings
    "Header A": "سرصفحه الف",
    "Header B": "سرصفحه ب",
    "Header C": "سرصفحه ج",
    "Header Extras": "اضافات سرصفحه",
    "Header Notification Bar": "نوار اطلاع‌رسانی سرصفحه",
    "Header Row": "ردیف سرصفحه",
    "Header Search": "جستجوی سرصفحه",
    "Header Text": "متن سرصفحه",
    "Header hidden": "سرصفحه پنهان",
    "Header notification bar": "نوار اطلاع‌رسانی سرصفحه",
    "Header overlay": "پوشش سرصفحه",
    "Header row": "ردیف سرصفحه",
    "Header wrap": "بسته‌بندی سرصفحه",
    "Heading IDs": "شناسه‌های سرفصل",
    "Heading link clicked": "پیوند سرفصل کلیک شد",
    "Heading tag": "برچسب سرفصل",
    "Height": "ارتفاع",
    "Height margin": "حاشیه ارتفاع",
    "Height transiton duration": "مدت زمان انتقال ارتفاع",
    "Help text": "متن کمکی",
    "Here you can add subtitles/captions to the media player.": "در اینجا می‌توانید زیرنویس‌ها/عنوان‌ها را به پخش‌کننده رسانه اضافه کنید.",
    "Hidden days": "روزهای پنهان",
    "Hide Header": "پنهان کردن سرصفحه",
    "Hide Nested Content in Builder": "پنهان کردن محتوای تودرتو در سازنده",
    "Hide at this breakpoint": "پنهان کردن در این نقطه شکست",
    "Hide button in builder": "پنهان کردن دکمه در سازنده",
    "Hide content in builder": "پنهان کردن محتوا در سازنده",
    "Hide header after scrolling": "پنهان کردن سرصفحه بعد از لغزش",
    "Hide if nothing to copy": "پنهان کردن اگر چیزی برای کپی کردن نیست",
    "Hide if zero": "پنهان کردن اگر صفر باشد",
    "Hide in builder": "پنهان کردن در سازنده",
    "Hide the sticky header after scrolling a certain distance": "پنهان کردن سرصفحه چسبناک بعد از لغزش فاصله معینی",
    "Hide until..": "پنهان کردن تا...",
    "Hiding controls": "کنترل‌های در حال پنهان‌سازی",
    "High volume": "صدای بلند",
    "Higher values = stops movement faster": "مقادیر بیشتر = توقف حرکت سریع‌تر",
    "Highlight Target Elements": "برجسته‌سازی عناصر هدف",
    "Hint": "نکته",
    "Horizontal gap": "شکاف افقی",
    "Horizontal position": "موقعیت افقی",
    "Horizontal split": "تقسیم افقی",
    "Hotspot Index": "شاخص نقطه داغ",
    "Hotspot debug": "اشکال‌زدایی نقطه داغ",
    "Hotspot name": "نام نقطه داغ",
    "Hotspots": "نقاط داغ",
    "Hours": "ساعت‌ها",
    "Hover element": "عنصر عبور",
    "Hover over another element": "عبور از عنصر دیگری",
    "Hover over this element": "عبور از این عنصر",
    "How events are rendered in grid views": "چگونه رویدادها در نمایش‌های شبکه ارائه می‌شوند",
    "How far before the slider comes into view.": "چقدر قبل از اینکه اسلایدر در دید ظاهر شود.",
    "How long to stay in copied state": "مدت زمان ماندن در حالت کپی شده",
    "How many pages around the active slide to load": "چند صفحه در اطراف اسلاید فعال برای بارگذاری",
    "Icon": "نماد",
    "Icon + Text": "نماد + متن",
    "Icon animation": "انیمیشن نماد",
    "Icon background": "پس‌زمینه نماد",
    "Icon border": "حاشیه نماد",
    "Icon box shadow": "سایه جعبه نماد",
    "Icon color": "رنگ نماد",
    "Icon only": "فقط نماد",
    "Icon padding": "آمادگی نماد",
    "Icon type": "نوع نماد",
    "Icon wrapper": "بسته‌بندی نماد",
    "If changing the items to li, set this to ul": "اگر آیتم‌ها را به li تغییر می‌دهید، این را روی ul قرار دهید",
    "If inside a query loop, use the ID of the other slider": "اگر درون یک حلقه پرسش هستید، از شناسه اسلایدر دیگری استفاده کنید",
    "If set to visible, set overflow hidden on the section": "اگر روی نمایان تنظیم شود، overflow را روی بخش پنهان کنید",
    "If using only one dataset": "اگر فقط از یک مجموعه داده استفاده می‌کنید",
    "Image Hotspot Marker": "نشانگر نقطه داغ تصویر",
    "Image Hotspots": "نقاط داغ تصویر",
    "Image hotspot selected": "نقطه داغ تصویر انتخاب شده",
    "Image hotspots": "نقاط داغ تصویر",
    "Image to Pin": "تصویر برای پین",
    "In favorites loop": "در حلقه علاقه‌مندی‌ها",
    "Inactive time": "زمان غیرفعال",
    "Include CPT archive link for taxonomies": "شامل کردن پیوند بایگانی CPT برای تاکسونومی‌ها",
    "Include Category": "شامل کردن دسته‌بندی",
    "Include Product Category": "شامل کردن دسته‌بندی محصول",
    "Include Shop Page": "شامل کردن صفحه فروشگاه",
    "Include all selectors where the cursor should turn into the hover state": "شامل کردن تمام انتخاب‌کننده‌هایی که در آن مکان‌نما باید به حالت عبور تبدیل شود",
    "Include home page link": "شامل کردن پیوند صفحه اصلی",
    "Include posts page link": "شامل کردن پیوند صفحه نوشته‌ها",
    "Include system option": "شامل کردن گزینه سیستم",
    "Independent scrolling": "لغزش مستقل",
    "Indicator": "شاخص",
    "Information": "اطلاعات",
    "Information messages": "پیام‌های اطلاعات",
    "Inherit": "ارث‌بری",
    "Initial": "اولیه",
    "Initial View": "نمایش اولیه",
    "Initial scroll time": "زمان لغزش اولیه",
    "Initial sort order": "ترتیب مرتب‌سازی اولیه",
    "Initial state": "حالت اولیه",
    "Inline mode allows breadcrumbs to wrap like regular text": "حالت درون‌خطی به ردپای نان اجازه می‌دهد مانند متن معمولی بپیچد",
    "Inner color": "رنگ درونی",
    "Inner content": "محتوای درونی",
    "Inner layout": "طرح درونی",
    "Inner spacing": "فاصله درونی",
    "Input indicator": "شاخص ورودی",
    "Input padding": "آمادگی ورودی",
    "Input type": "نوع ورودی",
    "Input wrapper": "بسته‌بندی ورودی",
    "Insert SVG": "درج SVG",
    "Inside this elements": "در داخل این عناصر",
    "Instruction text": "متن دستورالعمل",
    "Instruction text (optional)": "متن دستورالعمل (اختیاری)",
    "Instructions": "دستورالعمل‌ها",
    "Instructions text": "متن دستورالعمل‌ها",
    "Interaction": "تعامل",
    "Interactions": "تعاملات",
    "Interval": "فاصله",
    "Interval time": "زمان فاصله",
    "Intro": "مقدمه",
    "Intro text": "متن مقدمه",
    "Intro text (bottom)": "متن مقدمه (پایین)",
    "Intro text (top)": "متن مقدمه (بالا)",
    "Invalid license": "مجوز نامعتبر",
    "Invert": "معکوس",
    "Invisible": "نامرئی",
    "Invite participants": "دعوت شرکت‌کنندگان",
    "Is RTL": "آیا RTL است",
    "Is Taxonomy Archive": "آیا بایگانی تاکسونومی است",
    "Is active": "فعال است",
    "Is active (Any)": "فعال است (هر کدام)",
    "Is active (Exact)": "فعال است (دقیق)",
    "Is custom meta": "فیلد فلزی سفارشی است",
    "Is empty": "خالی است",
    "Is login": "ورود است",
    "Is logout": "خروج است",
    "Is password protected": "با رمز عبور محافظت شده است",
    "Is singular": "منفرد است",
    "Item": "آیتم",
    "Item added": "آیتم افزوده شد",
    "Item color": "رنگ آیتم",
    "Item counter": "شمارش‌گر آیتم",
    "Item height": "ارتفاع آیتم",
    "Item link": "پیوند آیتم",
    "Item padding": "آمادگی آیتم",
    "Item removed": "آیتم حذف شد",
    "Item selected": "آیتم انتخاب شده",
    "Item spacing": "فاصله آیتم",
    "Item width": "عرض آیتم",
    "Items": "آیتم‌ها",
    "Items per page": "آیتم‌ها در هر صفحه",
    "Italic": "کج",
    "ItalicText": "متن کج",
    "Justify text": "توجیه متن",
}

def apply_translations(input_file, output_file):
    """Apply translations to the PO file."""
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    result = []
    i = 0
    translated_count = 0
    skipped_count = 0

    while i < len(lines):
        line = lines[i]

        if line.startswith('msgid "'):
            msgid_match = re.match(r'msgid "(.*)"', line.strip())
            if msgid_match:
                msgid_text = msgid_match.group(1)
                result.append(line)
                i += 1

                # Check for msgstr
                if i < len(lines) and lines[i].startswith('msgstr'):
                    msgstr_match = re.match(r'msgstr "(.*)"', lines[i].strip())
                    if msgstr_match:
                        current_translation = msgstr_match.group(1)

                        # If empty, try to find translation
                        if current_translation == '':
                            if msgid_text in translations_dict:
                                result.append(f'msgstr "{translations_dict[msgid_text]}"\n')
                                translated_count += 1
                            else:
                                result.append(lines[i])
                                skipped_count += 1
                        else:
                            result.append(lines[i])
                    else:
                        result.append(lines[i])
                    i += 1
                else:
                    i += 1
            else:
                result.append(line)
                i += 1
        else:
            result.append(line)
            i += 1

    # Write the result
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(result)

    print(f"✅ Translation application completed!")
    print(f"📊 Translated: {translated_count} strings")
    print(f"⏭️  Skipped (already translated or no translation): {skipped_count} strings")
    print(f"💾 File saved: {output_file}")

if __name__ == "__main__":
    apply_translations("bricksextras-fa_IR.po", "bricksextras-fa_IR.po")
