"""
Author: Juan Carlos Miranda
Description:
    Script to show the use of strings to various languages.

    https://phrase.com/blog/posts/translate-python-gnu-gettext/
    https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    https://stackoverflow.com/questions/21044407/tkinter-app-allowing-for-multiple-languages
    https://stackoverflow.com/questions/3837683/python-no-translation-file-found-for-domain-using-custom-locale-folder

Usage:
    python python_language_i18n.py
"""
import locale
import gettext
import os

"""
Strings are saved in /locale/es_ES/LC_MESSAGES/gui_classes_ES.po.
The file "gui_classes.po" should be edited using (https://poedit.net/)[https://poedit.net/]
To use the string variable, call using the origin text, for example to use the string
"About" you should call _("About")

Compile "gui_classes_ES.po" using Poedit and put the new file "gui_classes_ES.mo" in the directory /locale/LC_MESSAGES/es_ES.

# Use the Poedit program to edit language strings https://poedit.net/
#
# locales/
# ├── es_ES
# │   └── LC_MESSAGES
# │       │── gui_classes_ES.po
# │       └── gui_classes_ES.mo
# └── en
#     └── LC_MESSAGES
#         │── gui_classes_EN.po
#         └── gui_classes_EN.mo
#

Requirements:

pip install python-gettext

"""

if __name__ == '__main__':
    current_locale, encoding = locale.getdefaultlocale()
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    locale_path = os.path.join(ROOT_PATH, 'locale')  # call to directory with configurations
    language = gettext.translation('gui_classes_ES', locale_path, ['es_ES'])
    language.install()
    print("---------------------------------------------------------------")
    print("Show strings saved in gui_classes.po applying es_ES translation")
    print("---------------------------------------------------------------")
    print(f"__file__ = {__file__}")
    print(f"current_locale={current_locale}")
    print(f"encoding={encoding}")
    print(f"LOCAL_PATH={ROOT_PATH}")
    print(f"locale_path={locale_path}")

    print(_("Remote console manager"))
    print(_("Remote camera console"))
    print(_("Enable remote clients"))
    print(_("Start record"))
    print(_("Stop record"))
    print(_("Shutdown remote clients"))
    print(_("Quit"))
    print(_("About..."))
    print(_("About"))
    print(_("Not implemented yet!!!"))
    print(_("Print enable clients"))
    print(_("Print enable record"))
    print(_("Shutdown clients"))

    language = gettext.translation('gui_classes_EN', locale_path, ['en'])
    language.install()
    print("---------------------------------------------------------------")
    print("Show strings saved in gui_classes.po applying es_ES translation")
    print("---------------------------------------------------------------")
    print(f"__file__ = {__file__}")
    print(f"current_locale={current_locale}")
    print(f"encoding={encoding}")
    print(f"LOCAL_PATH={ROOT_PATH}")
    print(f"locale_path={locale_path}")

    print(_("Remote console manager"))
    print(_("Remote camera console"))
    print(_("Enable remote clients"))
    print(_("Start record"))
    print(_("Stop record"))
    print(_("Shutdown remote clients"))
    print(_("Quit"))
    print(_("About..."))
    print(_("About"))
    print(_("Not implemented yet!!!"))
    print(_("Print enable clients"))
    print(_("Print enable record"))
    print(_("Shutdown clients"))





