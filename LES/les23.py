class Video:

    def create(self, name):
        self.name = name

    def play(self):
        print(f'Воспроизведение видео {self.name}')

class YouTube:

    lst_video = []

    @classmethod
    def add_video(cls, video):
        cls.lst_video.append(video)
    @classmethod

    def play_video(cls, video_index):
        cls.lst_video[video_index].play()

v1 = Video()
v2 = Video()

v1.create('Python')
v2.create('Python OOP')

youtube = YouTube()
youtube.add_video(v1)
youtube.add_video(v2)

youtube.play_video(0)
youtube.play_video(1)
