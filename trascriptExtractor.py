from youtube_transcript_api import YouTubeTranscriptApi
from foobardb import FoobarDB

videosList = []
transcript = []

# opens .txt with videos Ids and saves on videosList var
file = open("lista/videosId.txt", "r")
videosList = file.readlines()
file.close()

# Cleans \n breakdown from videosList var
count = 0
for i in videosList:

    videosList[count] = videosList[count].replace("\n", "")
    count += 1


# gets transcript from videos in videosList
count = 0
errorList = []
for videoId in videosList:

    try:
        transcript = YouTubeTranscriptApi.get_transcript(videoId, languages=["pt"])
    except:
        errorList.append(videoId)
        print(videoId)
        pass

    fulltext = ""
    # binds transcription together into fulltext var
    for i in transcript:
        fulltext = fulltext + " " + i["text"]

    # saves trascription into foobarDB
    mydb = FoobarDB("./mydb.db")
    mydb.set(videoId, fulltext)  # Sets Value
    count += 1
    print(count,". ",videoId)

# prints a list of videos that trasnscriptions could not be retrieved
print(errorList)
