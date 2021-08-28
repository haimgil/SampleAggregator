from ./classes import Sample
from ./classes import Session
from typing import Dict
import time

class Aggregator():
	"""docstring for Aggregator"""
	fiftin_min_ephoc = 15*60
	two_hours_ephoc = 120*60
	
	def __init__(self):
		super(Aggregator, self).__init__()
		self.samples:Dict[int ,tuple[Sample,int]] = {}
		
	def aggregate(self, sample) -> Optional[Session]:
	    return self.aggregate_samples(sample, False)

    def aggregate_with_lag(self, sample) -> Optional[Session]:
    	return self.aggregate_samples(sample, True)

    def aggregate_samples(self, sample, lag:bool):
    	if sample.machine_id in self.samples:
    		prevSample,timeRecieved = self.samples[sample.machine_id]
    		if self.same_session(sample, prevSample):
    			if self.is_session_open(lag, timeRecieved):
    				session = self.generate_session(prevSample, sample)
				else :
					session = self.generate_session(prevSample, None)
				return session
		self.samples[sample.machine_id] = (sample, time.time())


    def generate_session(self, prevSample, sample) -> Optional[Session]::
    	self.samples.pop(prevSample.machine_id, None)
		session = Session(prevSample, sample)
		return session

	def same_session(self, sample, prevSample) -> bool:
		return prevSample.measurementTime-sample.measurementTime <= Aggregator.fiftin_min_ephoc

	def is_session_open(self, lag, timeRecieved) -> bool:
		return not lag or lag and time.time() - timeRecieved <= Aggregator.two_hours_ephoc