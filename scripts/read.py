from obspy.core import read
stream = read('./data/fdsnws.mseed')
print stream
