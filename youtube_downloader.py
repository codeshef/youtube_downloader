import pytube


print "Enter the video link"

link = input()


yt = pytube.YouTube(link)


videos = yt.get_videos()

print yt.filename

s = 1
for v in videos:
    print(str(s)+"."+str(v) )
    s +=1

print "Enter the number of the videos : "
n = int(input())
vid = videos[n-1]

print("Enter the destination : ")

destination = input()
vid.download(destination)

print yt.filename+"\n has been successfully downloaded"