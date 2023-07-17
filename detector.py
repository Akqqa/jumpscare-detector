import librosa

y, sr = librosa.load("markiplier.mp3")

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