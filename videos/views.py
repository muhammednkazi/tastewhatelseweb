from django.shortcuts import render,redirect
from videos.models import video,videoComment
from django.contrib import messages

# Create your views here.
def videos(request):
    data=video.objects.all()
    return render(request,"videos/videos.html",{'data':data})
    # videos.html is a file in videos folder in templates folder

def openvideo(request,id): #id
    data=video.objects.filter(video_id=id)[0]
    comments=videoComment.objects.filter(video_id=data.video_id)
    user=request.user
    print(request.user)
    # [0] or .first() for getting the first object

    #for diplaying previous post if any
    if video.objects.filter(video_id= id-1):
        prev_post=video.objects.filter(video_id=id-1)[0]
        print(prev_post)
    else:
        print("no data found")
        prev_post=''


    #for diplaying next post if any
    if video.objects.filter(video_id=id+1):
        next_post=video.objects.filter(video_id=id+1)[0]
        print(next_post)
    else:
        print("no data found")
        next_post=''
    return render(request,'videos/openvideo.html',{'data':data,'prev_post':prev_post,'next_post':next_post,'comments':comments,'user':user})

def HandleComment(request):
    if request.method=='POST': 
        comment=request.POST.get("comment")
        video_id=request.POST.get("video_id") #accepting id of the video on which comment is done.
        video_id=video.objects.get(video_id=video_id) #fetching video id from the Video Table from the id which we have got through template.
        
        user=request.user #user who did the comment
        addcomment=videoComment(comment=comment,user=user,video_id=video_id)
        addcomment.save()
        messages.success(request, f'Comment Posted Successfully')
        return redirect(f"/videos/{video_id.video_id}")

    