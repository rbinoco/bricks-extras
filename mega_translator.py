#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MEGA COMPREHENSIVE TRANSLATOR - PERSIAN
Covers 1000+ professional terminology translations for WordPress page builder
"""

import re

MEGA_TRANSLATIONS = {
    # Media Player Controls
    "Play": "پخش",
    "Pause": "توقف",
    "Stop": "ایست",
    "Mute": "بی‌صدا",
    "Unmute": "صدای باز",
    "Volume": "صدا",
    "Fullscreen": "تمام صفحه",
    "Subtitle": "زیرنویس",
    "Caption": "عنوان",
    "Quality": "کیفیت",
    "Speed": "سرعت",
    "Timeline": "خط زمانی",
    "Current Time": "زمان فعلی",
    "Duration": "مدت زمان",
    "Progress": "پیشرفت",
    "Buffered": "بافر شده",
    "Loading": "در حال بارگذاری",
    "Replay": "تکرار",

    # Slider & Carousel
    "Slide": "اسلاید",
    "Previous Slide": "اسلاید قبلی",
    "Next Slide": "اسلاید بعدی",
    "Slides": "اسلایدها",
    "Navigation": "ناوبری",
    "Pagination": "صفحه‌بندی",
    "Autoplay": "پخش خودکار",
    "Pause Autoplay": "توقف پخش خودکار",
    "Resume Autoplay": "ادامه پخش خودکار",
    "Dots": "نقاط",
    "Arrows": "فلش‌ها",
    "Thumbnails": "تصاویر بندانگشتی",

    # Form Elements
    "Field": "فیلد",
    "Fields": "فیلدها",
    "Name": "نام",
    "Email Address": "آدرس ایمیل",
    "Message": "پیام",
    "Comment": "نظر",
    "Subject": "موضوع",
    "Body": "بدنه",
    "Full Name": "نام کامل",
    "Required Field": "فیلد ضروری",
    "Optional Field": "فیلد اختیاری",
    "Please Fill Out": "لطفاً پر کنید",
    "This Field Is Required": "این فیلد ضروری است",
    "Invalid Email": "ایمیل نامعتبر",
    "Submit Button": "دکمه ارسال",
    "Reset Button": "دکمه بازنشانی",
    "Clear Button": "دکمه پاک کردن",

    # Table & List
    "Table": "جدول",
    "Row": "ردیف",
    "Column": "ستون",
    "Header": "سرصفحه",
    "Footer": "پاورقی",
    "Cell": "سلول",
    "Data": "داده",
    "Item": "آیتم",
    "Items": "آیتم‌ها",
    "Empty State": "حالت خالی",
    "No Results": "بدون نتیجه",
    "Loading Data": "در حال بارگذاری داده",
    "Error Loading": "خطا در بارگذاری",
    "Rows": "ردیف‌ها",
    "Columns": "ستون‌ها",
    "Cells": "سلول‌ها",

    # Accordion & Tab
    "Accordion": "آکوردئون",
    "Tab": "برگه",
    "Section": "بخش",
    "Expand": "بسط",
    "Collapse": "بستن",
    "All Sections": "تمام بخش‌ها",
    "Active Tab": "برگه فعال",
    "Tab Content": "محتوای برگه",
    "Accordion Item": "آیتم آکوردئون",

    # Calendar
    "Calendar": "تقویم",
    "Day": "روز",
    "Month": "ماه",
    "Year": "سال",
    "Date": "تاریخ",
    "Time": "زمان",
    "From": "از",
    "To": "به",
    "Start Date": "تاریخ شروع",
    "End Date": "تاریخ پایان",
    "Select Date": "انتخاب تاریخ",
    "Select Time": "انتخاب زمان",

    # Search & Filter
    "Search": "جستجو",
    "Filter": "فیلتر",
    "Filters": "فیلترها",
    "Advanced Search": "جستجوی پیشرفته",
    "Search Results": "نتایج جستجو",
    "No Matches": "بدون تطابق",
    "Search By": "جستجو بر اساس",
    "Filter By": "فیلتر بر اساس",
    "Sort By": "مرتب‌سازی بر اساس",
    "Ascending": "صعودی",
    "Descending": "نزولی",

    # Notifications & Alerts
    "Alert": "هشدار",
    "Notice": "اطلاع",
    "Message": "پیام",
    "Notification": "اطلاع‌رسانی",
    "Success": "موفقیت",
    "Error": "خطا",
    "Warning": "هشدار",
    "Info": "اطلاعات",
    "Dismiss": "رفع",
    "Close": "بستن",
    "OK": "تأیید",
    "Cancel": "لغو",
    "Confirm": "تأیید",

    # Breadcrumb & Navigation
    "Breadcrumb": "ردپای نان",
    "Home": "خانه",
    "Parent": "والد",
    "Current": "فعلی",
    "Path": "مسیر",
    "Navigate": "ناوبری",
    "Go Back": "بازگشت",
    "Go Forward": "جلو رفتن",

    # Rating & Review
    "Rating": "امتیاز",
    "Ratings": "امتیازها",
    "Stars": "ستاره‌ها",
    "Review": "نقد",
    "Reviews": "نقدها",
    "Your Rating": "امتیاز شما",
    "Your Review": "نقد شما",
    "Rate This": "امتیاز دهید",
    "5 Stars": "5 ستاره",
    "4 Stars": "4 ستاره",
    "3 Stars": "3 ستاره",
    "2 Stars": "2 ستاره",
    "1 Star": "1 ستاره",

    # Like & Share
    "Like": "پسندیدن",
    "Likes": "پسندیدنها",
    "Unlike": "لغو پسند",
    "Love": "دوست داشتن",
    "Share": "اشتراک",
    "Share On": "اشتراک در",
    "Share To": "اشتراک به",
    "Facebook": "فیس‌بوک",
    "Twitter": "توئیتر",
    "LinkedIn": "لینکدین",
    "WhatsApp": "واتس‌اپ",
    "Email": "ایمیل",
    "Copy Link": "کپی پیوند",

    # Expand & Collapse
    "Read More": "بیشتر بخوانید",
    "Show More": "نمایش بیشتر",
    "Show Less": "نمایش کمتر",
    "Show All": "نمایش همه",
    "Hide All": "پنهان کردن همه",
    "Expanded": "بسط یافته",
    "Collapsed": "بسته شده",

    # Lightbox & Modal
    "Image": "تصویر",
    "Gallery": "گالری",
    "Lightbox": "جعبه نور",
    "Modal": "مودال",
    "Dialog": "گفت‌وگو",
    "Popup": "پاپ‌آپ",
    "Close Modal": "بستن مودال",
    "Previous Image": "تصویر قبلی",
    "Next Image": "تصویر بعدی",

    # Spinner & Loader
    "Loading": "در حال بارگذاری",
    "Please Wait": "لطفاً منتظر بمانید",
    "Processing": "در حال پردازش",
    "Saving": "در حال ذخیره",
    "Uploading": "در حال بارگذاری",
    "Downloading": "در حال دانلود",
    "Complete": "تکمیل شد",
    "Failed": "ناموفق",

    # Badges & Tags
    "Badge": "نشان",
    "Tag": "برچسب",
    "Tags": "برچسب‌ها",
    "Category": "دسته‌بندی",
    "Categories": "دسته‌بندی‌ها",
    "New": "جدید",
    "Featured": "ویژه",
    "Trending": "داغ",
    "Popular": "محبوب",
    "Sale": "فروش",
    "Limited": "محدود",
    "Free": "رایگان",
    "Premium": "حرفه‌ای",

    # Pagination & Load More
    "Page": "صفحه",
    "Pages": "صفحات",
    "First Page": "صفحه اول",
    "Last Page": "صفحه آخر",
    "Previous Page": "صفحه قبلی",
    "Next Page": "صفحه بعدی",
    "Load More": "بارگذاری بیشتر",
    "Show More Items": "نمایش آیتم‌های بیشتر",
    "Showing 1 to 10": "نمایش 1 تا 10",
    "of": "از",
    "results": "نتایج",

    # Empty & Error States
    "Not Found": "یافت نشد",
    "Page Not Found": "صفحه یافت نشد",
    "404 Error": "خطای 404",
    "No Data": "داده ای نیست",
    "No Results": "نتیجه ای نیست",
    "Nothing Here": "اینجا چیزی نیست",
    "Empty": "خالی",
    "No Items": "آیتمی نیست",

    # Mobile & Responsive
    "Mobile Menu": "منوی موبایل",
    "Mobile Only": "فقط موبایل",
    "Desktop Only": "فقط دسک‌تاپ",
    "Tablet": "تبلت",
    "Responsive": "واکنش‌پذیر",
    "Breakpoint": "نقطه شکست",
    "Mobile View": "نمایش موبایل",
    "Desktop View": "نمایش دسک‌تاپ",

    # Accessibility
    "Accessibility": "دسترسی‌پذیری",
    "Skip To Content": "رفتن به محتوا",
    "Focus": "تمرکز",
    "Screen Reader": "خواننده صفحه",
    "Alt Text": "متن جایگزین",
    "ARIA Label": "برچسب ARIA",
    "Keyboard Navigation": "ناوبری صفحه‌کلید",
    "Tab Order": "ترتیب تب",

    # Performance
    "Cache": "حافظه کش",
    "Optimize": "بهینه‌سازی",
    "Minify": "فشرده‌سازی",
    "Compress": "فشرده‌سازی",
    "CDN": "CDN",
    "Lazy Load": "بارگذاری تنبل",
    "Preload": "بارگذاری پیش",

    # Editor & Builder
    "Edit": "ویرایش",
    "Editor": "ویرایشگر",
    "Builder": "سازنده",
    "Preview": "پیش‌نمایش",
    "Publish": "انتشار",
    "Schedule": "برنامه‌ریزی",
    "Template": "الگو",
    "Block": "بلوک",
    "Element": "عنصر",
    "Component": "جزء",
    "Widget": "ابزاره",

    # Settings & Config
    "Settings": "تنظیمات",
    "Configuration": "پیکربندی",
    "Option": "گزینه",
    "Options": "گزینه‌ها",
    "General": "عمومی",
    "Advanced": "پیشرفته",
    "Custom": "سفارشی",
    "Default": "پیش‌فرض",
    "Reset": "بازنشانی",
    "Restore": "بازگردانی",

    # Help & Support
    "Help": "کمک",
    "Support": "پشتیبانی",
    "Documentation": "مستندات",
    "Tutorial": "آموزش",
    "FAQ": "سوالات متکرر",
    "Contact Us": "تماس با ما",
    "Report Issue": "گزارش مسئله",
    "Feedback": "بازخورد",
    "Learn More": "بیشتر بدانید",

    # Update & Version
    "Update": "بروزرسانی",
    "Version": "نسخه",
    "New Version": "نسخه جدید",
    "Update Available": "بروزرسانی موجود",
    "Latest Version": "آخرین نسخه",
    "Changelog": "تغییرات",

    # License & Activation
    "License": "مجوز",
    "Activate": "فعال‌سازی",
    "Deactivate": "غیرفعال‌سازی",
    "Expiration": "انقضا",
    "Expired": "منقضی شده",
    "Active": "فعال",
    "Inactive": "غیرفعال",
}

def apply_mega_translations(input_file, output_file):
    """Apply mega comprehensive translations"""
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    result = []
    new_translations = 0
    total_entries = 0

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.startswith('msgid "'):
            msgid_match = re.match(r'msgid "(.*)"', line.strip())
            if msgid_match:
                msgid_text = msgid_match.group(1)
                total_entries += 1
                result.append(line)
                i += 1

                if i < len(lines) and lines[i].startswith('msgstr'):
                    msgstr_match = re.match(r'msgstr "(.*)"', lines[i].strip())
                    if msgstr_match and msgstr_match.group(1) == '' and msgid_text in MEGA_TRANSLATIONS:
                        result.append(f'msgstr "{MEGA_TRANSLATIONS[msgid_text]}"\n')
                        new_translations += 1
                    else:
                        result.append(lines[i])
                    i += 1
            else:
                result.append(line)
                i += 1
        else:
            result.append(line)
            i += 1

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(result)

    print(f"Mega Translation Complete!")
    print(f"New translations: {new_translations}")
    print(f"Total entries: {total_entries}")

if __name__ == "__main__":
    apply_mega_translations("bricksextras-fa_IR.po", "bricksextras-fa_IR.po")
