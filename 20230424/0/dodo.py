import glob

DOIT_CONFIG = {'default_tasks': ['all']} 

def task_pot():
	return {
		'actions': ['pybabel extract -o counter.pot counter.py '],
		'file_dep': ['counter.py'],
		'targets': ['counter.pot']  # файл существует; новее dep и является результатом выполнения задания
		}

def task_po():
	return {
		'actions': ['pybabel update -D counter -d po -i counter.pot -l ru'],
		'file_dep': ['counter.pot'],
		'targets': ['po/ru/LC_MESSAGES/counter.po']
		}

def task_mo():
	return {
		'actions': ['pybabel compile -D counter -d po -l ru'],
		'file_dep': ['po/ru/LC_MESSAGES/counter.po'],
		'targets': ['po/ru/LC_MESSAGES/counter.mo'],
	}
		
def task_test():
    return{
		'actions': ['python3 unittest -v test_counter.py'],
		'file_dep': ['test_counter.py']
	}
