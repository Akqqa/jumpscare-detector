import librosa
import matplotlib.pyplot as plt
import datetime

y, sr = librosa.load("markiplier.mp3")

# librosa.display.waveshow(y=y, sr=sr)
# plt.show()

# Not good, detects 1075 onsets in the 7 minute clip
results = librosa.onset.onset_detect(y=y, sr=sr, units='time')

print(len(results))

# Exactly the same lmfao
o_env = librosa.onset.onset_strength(y=y, sr=sr)
times = librosa.times_like(o_env, sr=sr)
onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr)
onset_times = librosa.frames_to_time(onset_frames)
print(len(onset_times))

# Attempting to detect peaks specifically - IT FINDS EVEN MORE ;.; WAIT NO it finds way less if we increase all pres/posts to a few hundred

peaks = librosa.util.peak_pick(o_env, pre_max=400, post_max=400, pre_avg=400, post_avg=400, delta=0.5, wait=5)
peak_seconds = librosa.frames_to_time(peaks)
print(len(peak_seconds))

print(peak_seconds)

# not actually detecting the jumpscares :(((


length = librosa.get_duration(y=y, sr=sr)
number_samples = length * sr
print(number_samples)

peaks = librosa.util.peak_pick(o_env, pre_max=number_samples/100, post_max=number_samples/100, pre_avg=number_samples/100, post_avg=number_samples/100, delta=0.5, wait=5)
peak_seconds = librosa.frames_to_time(peaks)
print(peak_seconds)

# TRY REDUCING SAMPKLES PER SECOND TO LIKE 2 LMAO

y_5 = librosa.resample(y, orig_sr=sr, target_sr=15)
print(y_5.shape)



results = librosa.onset.onset_detect(y=y_5, sr=15, units='time')
print("b:" + str(len(results)))

o_env = librosa.onset.onset_strength(y=y_5, sr=15)

peaks = librosa.util.peak_pick(y_5, pre_max=5, post_max=5, pre_avg=5, post_avg=5, delta=0.01, wait=100)
peak_seconds = librosa.frames_to_time(peaks, sr=15, hop_length=1)
print(len(peak_seconds))
print(peak_seconds)

print([str(datetime.timedelta(seconds=x)) for x in peak_seconds])

librosa.display.waveshow(y=y_5, sr=15)
plt.show()# YOU CAN CLEARLY SEE THE JUMPSCARES SO WHY ISNT PEAKS DETECTING ANY ??

print(librosa.get_duration(y=y_5, sr=15))

# YO IT WORKS>>!??!?