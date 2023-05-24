from doit.task import clean_targets
import shutil


DOIT_CONFIG = {'default_tasks': ['html']}


def task_pot():
	"""Extract translation"""
	return {
		'actions': ['pybabel extract --input-dirs moodserver/moodserver -o moodserver/moodserver/moodserver.pot', 'cp po_sample moodserver/moodserver/po/ru/LC_MESSAGES/moodserver.po'],
		'targets': ['moodserver/moodserver/moodserver.pot'],
		'clean': True,
		}

def task_po():
	"""Update translation"""
	return {
		'actions': ['pybabel update -D moodserver -d moodserver/moodserver/po -i moodserver/moodserver/moodserver.pot', 'cp po_sample moodserver/moodserver/po/ru/LC_MESSAGES/moodserver.po'],
		'file_dep': ['moodserver/moodserver/moodserver.pot'],
		'targets': ['moodserver/moodserver/po/ru/LC_MESSAGES/moodserver.po'],
		'clean': True,
		}

def task_i18n():
	"""Compile translation"""
	return {
		'actions': ['pybabel compile -d moodserver/moodserver/po -D moodserver'],
		'file_dep': ['moodserver/moodserver/po/ru/LC_MESSAGES/moodserver.po'],
		'targets': ['moodserver/moodserver/po/ru/LC_MESSAGES/moodserver.mo'],
		'clean': True,
		}

def task_test():
	"""Test MOOD"""
	return {
		'actions':['python3 -m unittest -v test_game.py'],
		'file_dep': ['test_game.py'],
		'task_dep': ['i18n'],
		'clean': True,
		}

def task_html():
	"""Make documentation"""
	return {
		'actions': ['make -C docs html'],
		'task_dep': ['i18n'],
		'targets': ['docs/build'],
		'clean': [lambda: shutil.rmtree('docs/build')],
		}
		
def task_whlserver():
	"""Make server wheel"""
	return {
		'actions': ['python3 -m build -n -w moodserver'],
		'task_dep': ['i18n'],
		'file_dep': ['moodserver/pyproject.toml', 'moodserver/moodserver/po/ru/LC_MESSAGES/moodserver.mo'],
		'targets': ['moodserver/dist/*.whl'],
		'clean': [lambda: shutil.rmtree('moodserver/dist'), lambda: shutil.rmtree('moodserver/build'), lambda: shutil.rmtree('moodserver/MoodServer.egg-info')],
		}

def task_whlclient():
	"""Make client wheel"""
	return {
		'actions': ['python3 -m build -n -w moodclient'],
		'file_dep': ['moodclient/pyproject.toml'],
		'targets': ['moodclient/dist/*.whl'],
		'clean': [lambda: shutil.rmtree('moodclient/dist'), lambda: shutil.rmtree('moodclient/build'), lambda: shutil.rmtree('moodclient/MoodClient.egg-info')],
		}

def task_wheels():
	"""Make wheels"""
	return {
		'actions': None,
		'task_dep': ['whlserver', 'whlclient'],
		}
