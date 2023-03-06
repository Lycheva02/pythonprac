import cmd
import shlex
import calendar

class Calend(cmd.Cmd):
	
	def do_prmonth(self, args):
		'''Print a month’s calendar as returned by formatmonth().'''
		y, m = tuple(map(int, shlex.split(args)))
		print(calendar.prmonth(y, m))
	
	def complete_prmonth(self, prefix, line, start, end):
		if len(shlex.split(line)) < 3 and not line[-1].isspace():
			return list()
		variants = [i for i in range(1, 13)]
		return [str(i) for i in variants if str(i).startswith(prefix)]
		
		
C = Calend()
C.cmdloop()
