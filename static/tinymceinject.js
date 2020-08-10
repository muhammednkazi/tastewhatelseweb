//this js file is created for writing content of the video in the admin panel using tinymce editor.

var script=document.createElement('script');
script.type='text/javascript';
script.src="https://cdn.tiny.cloud/1/78lcibq64vyz8nq5nwzwdsderkj8dnak89qqw0bk1jha5e8x/tinymce/5/tinymce.min.js";
document.head.appendChild(script);

script.onload = function(){
tinymce.init({
    selector: '#id_content',
    plugins: 'a11ychecker advcode casechange formatpainter linkchecker autolink lists checklist media mediaembed pageembed permanentpen powerpaste table advtable tinycomments tinymcespellchecker',
    toolbar: 'a11ycheck addcomment showcomments casechange checklist code formatpainter pageembed permanentpen table',
    toolbar_mode: 'floating',
    tinycomments_mode: 'embedded',
    tinycomments_author: 'Author name'
});
}