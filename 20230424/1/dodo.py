from doit.task import clean_targets
import shutil


DOIT_CONFIG = {'default_tasks': ['html']}


def task_pot():
	"""Extract translation"""
	return {
		'actions': ['pybabel extract --input-dirs moodserver/ -o moodserver/moodserver.pot'],
		'targets': ['moodserver/moodserver.pot'],
		}

def task_po():
	"""Update translation"""
	return {
		'actions': ['pybabel update -D moodserver -d moodserver/po -i moodserver/moodserver.pot'],
		'file_dep': ['moodserver/moodserver.pot'],
		'targets': ['moodserver/po/ru/LC_MESSAGES/moodserver.po'],
		}

def task_i18n():
	"""Compile translation"""
	return {
		'actions': ['pybabel compile -d moodserver/po -D moodserver'],
		'file_dep': ['moodserver/po/ru/LC_MESSAGES/moodserver.po'],
		'targets': ['moodserver/po/ru/LC_MESSAGES/moodserver.mo'],
		'clean': True,
		}
