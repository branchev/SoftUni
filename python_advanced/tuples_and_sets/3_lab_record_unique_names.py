def printing(recordings):
    for name in recordings:
        print(name)


def name_recordings(n):
    recordings = set()
    for _ in range(n):
        recordings.add(input())
    printing(recordings)


n = int(input())
name_recordings(n)
