from django.core.management.base import BaseCommand, CommandError
from video.models import Video
import os
import subprocess

class Command(BaseCommand):
    help = "Optimize Video"

    def handle(self, *args, **kwargs):
        try:
            print('#################Started Encoding#################')
            obj = Video.objects.filter(status ='Pending').first()
            if obj:
                # print('Changed the object to processing status')
                # obj.status = "Processing"
                # obj.is_running = True
                # obj.save()
                
                print('Copied input path from db')
                input_video_path = obj.video.path

                print('Set the output directory for saving hls files')
                output_directory = os.path.join(os.path.dirname(input_video_path), 'hls_output')
                os.makedirs(output_directory, exist_ok=True)
                output_filename = os.path.splitext(os.path.basename(input_video_path))[0] + '_hls.m3u8'
                output_hls_path = os.path.join(output_directory, output_filename)
                output_thumbnail_path = os.path.join(output_directory, os.path.splitext(os.path.basename(input_video_path))[0]+'thumbnail.jpg')

                print('Extracting important information from the video')
                cmd_duration = [
                    'ffprobe', '-v', 'quiet',
                    '-print_format', 'json', 
                    'show_streams',

                    input_video_path
                ]
                # result = subprocess.run(cmd_duration, shell= False, check= True, stdout=subprocess.pipe)
                ps= subprocess.Popen(cmd_duration, stdout=subprocess.PIPE)
                result  = subprocess.check_output(('grep', 'process_name'), stdin=ps.stdout)
                ps.wait()
                print(result.decode('uts-8'))

                # print('Encoding the video, please wait!!!')
                # cmd =[
                #     'ffmpeg',
                #     '-i',
                #     input_video_path,
                #     '-c:v',
                #     'h264',
                #     '-c:a',
                #     'aac',
                #     '-hls_time',
                #     '5',
                #     '-hls_list_size',
                #     '0',
                #     '-hls_base_url',
                #     '{{ dynamic_path }}/',
                #     '-movflags',
                #     '+faststart',
                #     '-y',
                #     output_hls_path
                # ]
                # subprocess.run(cmd, check=True)

                # print('Encoding Successful \n Change obj status to completed')
                # obj.hls = output_hls_path
                # obj.status = "Completed"
                # obj.is_running = False
                # obj.save()

        except Exception as e:
            print('Exception ala re:', e)