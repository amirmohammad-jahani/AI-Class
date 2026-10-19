playlist = ["Shape of you", "Blinding Lights", "Beliver", "Perfect"]

print(len(playlist))

print(f"First song : {playlist[0]} &  Last song : {playlist[-1]}")

playlist.append("Dynamitte")

playlist.remove("Beliver")

playlist.sort()
count = 1
for i in playlist:
    print(f"[{count}] {i}")
    count+=1

