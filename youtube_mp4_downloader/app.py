import sys

from pytube import YouTube

class YoutubeDownloader:
    def __init__(self):
        pass

    def download_song(self, url: str, output_path: str) -> None:
        try:
            data = YouTube(url)
            audio_data = data.streams.filter(only_audio=True).first()
            audio_title = audio_data.title
            audio_data.download(output_path)
            print(f'Successfully downloaded audio: {audio_title} to {output_path}')
        except Exception as e:
            print(f'Error: {e}')

    def get_commands(self):
        return sys.argv

    def execute(self):
        commands = self.get_commands()
        default_location = 'Songs/'
        error_msg = """
            Youtube Downloader
            Help
            1st param url --> E.g. https://www.youtube.com/watch?v=
            2nd param location to dump songs (by default goes to Song Directory)
        """
        if len(commands) == 2 and commands[1] == '--help':
            print(error_msg)

        if len(commands) == 3:
            url = commands[1]
            location = commands[2]
            self.download_song(url, location)

        elif len(commands) == 2:
            url = commands[1]
            self.download_song(url, default_location)

        else:
            raise Exception(error_msg)

if __name__ == '__main__':        
    yt = YoutubeDownloader()
    yt.execute()