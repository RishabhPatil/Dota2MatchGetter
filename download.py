import os

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__)) + "\\"

class MatchGetter:

	def __init__(self, start_match_id=None, start_seq_no=None):
		self.start_match_id = start_match_id
		self.start_seq_no = start_seq_no

	def load_config(self, filename=None, path=None):
		if filename and os.path.isfile(CURRENT_PATH+filename):
			with open(CURRENT_PATH+filename,'r') as f:
				self.config = json.load(f)
		if path and os.path.isfile(path):
			with open(path,'r') as f:
				self.config = json.load(f)

