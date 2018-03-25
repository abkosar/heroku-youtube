def index():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>YouTube Downloader</title>
<style>
    @import url('https://fonts.googleapis.com/css?family=Rye');
    body{
    background: black;
    color: white;
    animation-name: body-back;
    animation-duration:2s;
    animation-delay:2s;
    animation-fill-mode: forwards;
    }
    h1{
    font-size: 75px;
    font-family: 'Rye', cursive;
    }
    h3{
    color: black;
    animation-name: h3_color;
    animation-duration:2s;
    animation-delay:1s;
    animation-fill-mode: forwards;
    }
    .menu{
    font-size: 50px;
    color: white;
    font-family: 'Rye', cursive;
    text-decoration: none;
    animation-name: go-back;
    animation-duration:2s;
    animation-delay:1s;
    animation-fill-mode: forwards;
    }
    #form {
    font-family: 'Rye', cursive;
    color: white;
    background: black;
    border: 2px solid white;
    font-size: 25px;
    margin: 15px;
    margin-bottom: 50px;
    animation-name: form-location;
    animation-duration:2s;
    animation-delay:1s;
    animation-fill-mode: forwards;
    }
    #input{
    font-family: 'Rye', cursive;
    color: white;
    background: black;
    border: 2px solid white;
    font-size: 25px;
    margin-left: 45px;
    margin-bottom: 50px;
    animation-name: input-location;
    animation-duration:3s;
    animation-delay:1s;
    animation-fill-mode: forwards;
    }
    ::placeholder {
    color: red;
    opacity: 1;
    }
    #yt{
        margin-top: 10%;
        animation-name: ytube;
        animation-duration:2s;
        animation-delay:1s;
        animation-fill-mode: forwards;
    }
    @keyframes ytube{
        100%{
            color: red;
        }
    }
    @keyframes h3_color{
        100%{
            color: black;
        }
    }
    @keyframes body-back{
        100%{
            background-color: white;
        }
    }	
    @keyframes go-back{
        100%{
            color: red;
        }
    }
    @keyframes input-location{
        50%{
            color: red;
            background-color: white;
        }
        100%{
            color: red;
            background-color: white;
        }
    }
    @keyframes form-location {
        100%{
            color: red;
            background-color: white;
        }
    }
</style>
</head>
<body align="center">
<h1 id="yt">YouTube</h1><br>
<form method="POST" action="/search-youtube">
<input type="text" id="form" placeholder="song or url..." name="search_youtube"/>
<input type="submit" id="input" value="Search"/>
</form>
</body>
</html>
    """

def video_details():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=0.7">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{} - Youtube Downloader</title>
    <style>
        #homepage{{
        margin-top: 10%;
        color: red;
        font-size: 30px;
        }}
        a:visited{{
        color: red;
        }}
        #form {{
        border: white;
        font-size: 25px;
        margin-bottom: 20px;
        }}
        #input{{
        border: white;
        background: white;
        font-size: 25px;
        margin-left: 45px;
        }}
    </style>
</head>
<body align="center">
    <form method="POST" action="/search-youtube">
    <input type="text" id="form" placeholder="song or url..." name="search_youtube"/>
    <input type="submit" id="input" value="Search"/>
    </form>
    <table border="5px" align="center">
        <tr>
            <td colspan="2"><video width="500" height="280" controls><source src="{}" type="video/mp4"></video></td>
        </tr>
        <tr>
            <td>Video Name</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Duration</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>MP4 720P Video</td>
            <td><a href="{}">{}</a></td>
        </tr>
        <tr>
            <td>MP4 360P Video</td>
            <td><a href="{}">Download</a></td>
        </tr>
        <tr>
            <td>M4A Audio</td>
            <td><audio src="{}" controls/>
        </tr>
    </table>
    <footer id="homepage"><a href="/"><<< HomePage</a></footer>
</body>
</html>
    """

def yt_list():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>{} - YouTube Downloader</title>
<style>
        #submitForm0 input{{
        background: url("{}");
        font-size: 0px;
        width: 320px;
        height: 180px;
        }}
        #submitForm1 input{{
        background: url("{}");
        font-size: 0px;
        width: 320px;
        height: 180px;
        }}
        #submitForm2 input{{
        background: url("{}");
        font-size: 0px;
        width: 320px;
        height: 180px;
        }}
        #submitForm3 input{{
        background: url("{}");
        font-size: 0px;
        width: 320px;
        height: 180px;
        }}
        #submitForm4 input{{
        background: url("{}");
        font-size: 0px;
        width: 320px;
        height: 180px;
        }}
        #submitForm5 input{{
        background: url("{}");
        font-size: 0px;
        width: 320px;
        height: 180px;
        }}
        #submitForm6 input{{
        background: url("{}");
        font-size: 0px;
        width: 320px;
        height: 180px;
        }}
        #submitForm7 input{{
        background: url("{}");
        font-size: 0px;
        width: 320px;
        height: 180px;
        }}
        #submitForm8 input{{
        background: url("{}");
        font-size: 0px;
        width: 320px;
        height: 180px;
        }}
        #submitForm9 input{{
        background: url("{}");
        font-size: 0px;
        width: 320px;
        height: 180px;
        }}
        #submitForm10 input{{
        background: url("{}");
        font-size: 0px;
        width: 320px;
        height: 180px;
        }}
        #submitForm11 input{{
        background: url("{}");
        font-size: 0px;
        width: 320px;
        height: 180px;
        }}
        #submitForm12 input{{
        background: url("{}");
        font-size: 0px;
        width: 320px;
        height: 180px;
        }}
        #submitForm13 input{{
        background: url("{}");
        font-size: 0px;
        width: 320px;
        height: 180px;
        }}
        #submitForm14 input{{
        background: url("{}");
        font-size: 0px;
        width: 320px;
        height: 180px;
        }}
        #submitForm15 input{{
        background: url("{}");
        font-size: 0px;
        width: 320px;
        height: 180px;
        }}
        #submitForm16 input{{
        background: url("{}");
        font-size: 0px;
        width: 320px;
        height: 180px;
        }}
        #submitForm17 input{{
        background: url("{}");
        font-size: 0px;
        width: 320px;
        height: 180px;
        }}
        #submitForm18 input{{
        background: url("{}");
        font-size: 0px;
        width: 320px;
        height: 180px;
        }}
        #submitForm19 input{{
        background: url("{}");
        font-size: 0px;
        width: 320px;
        height: 180px;
        }}
        #submitForm20 input{{
        background: url("{}");
        font-size: 0px;
        width: 320px;
        height: 180px;
        }}
        #form {{
        border: white;
        font-size: 25px;
        }}
        #input{{
        border: white;
        background: white;
        font-size: 25px;
        margin-left: 45px;
        }}
</style>
</head>
<body align="center">
    <form method="POST" action="/search-youtube">
    <input type="text" id="form" placeholder="song or url..." name="search_youtube"/>
    <input type="submit" id="input" value="Search"/></form>
    <h2 style="text-align:center;">Results for "{}":</h2><br>
    <form method="POST" action="/video-details">
    <div id="submitForm0">
        <input type="submit" value="{}" name="youtube_id"><br><br>
        <yt>{} - {}</yt>
    </div><br>
    <div id="submitForm1">
        <input type="submit" value="{}" name="youtube_id"><br><br>
        <yt>{} - {}</yt>
    </div><br>
    <div id="submitForm2">
        <input type="submit" value="{}" name="youtube_id"><br><br>
        <yt>{} - {}</yt>
    </div><br>
    <div id="submitForm3">
        <input type="submit" value="{}" name="youtube_id"><br><br>
        <yt>{} - {}</yt>
    </div><br>
    <div id="submitForm4">
        <input type="submit" value="{}" name="youtube_id"><br><br>
        <yt>{} - {}</yt>
    </div><br>
    <div id="submitForm5">
        <input type="submit" value="{}" name="youtube_id"><br><br>
        <yt>{} - {}</yt>
    </div><br>
    <div id="submitForm6">
        <input type="submit" value="{}" name="youtube_id"><br><br>
        <yt>{} - {}</yt>
    </div><br>
    <div id="submitForm7">
        <input type="submit" value="{}" name="youtube_id"><br><br>
        <yt>{} - {}</yt>
    </div><br>
    <div id="submitForm8">
        <input type="submit" value="{}" name="youtube_id"><br><br>
        <yt>{} - {}</yt>
    </div><br>
    <div id="submitForm9">
        <input type="submit" value="{}" name="youtube_id"><br><br>
        <yt>{} - {}</yt>
    </div><br>
    <div id="submitForm10">
        <input type="submit" value="{}" name="youtube_id"><br><br>
        <yt>{} - {}</yt>
    </div><br>
    <div id="submitForm11">
        <input type="submit" value="{}" name="youtube_id"><br><br>
        <yt>{} - {}</yt>
    </div><br>
    <div id="submitForm12">
        <input type="submit" value="{}" name="youtube_id"><br><br>
        <yt>{} - {}</yt>
    </div><br>
    <div id="submitForm13">
        <input type="submit" value="{}" name="youtube_id"><br><br>
        <yt>{} - {}</yt>
    </div><br>
    <div id="submitForm14">
        <input type="submit" value="{}" name="youtube_id"><br><br>
        <yt>{} - {}</yt>
    </div><br>
    <div id="submitForm15">
        <input type="submit" value="{}" name="youtube_id"><br><br>
        <yt>{} - {}</yt>
    </div><br>
    <div id="submitForm16">
        <input type="submit" value="{}" name="youtube_id"><br><br>
        <yt>{} - {}</yt>
    </div><br>
    <div id="submitForm17">
        <input type="submit" value="{}" name="youtube_id"><br><br>
        <yt>{} - {}</yt>
    </div><br>
    <div id="submitForm18">
        <input type="submit" value="{}" name="youtube_id"><br><br>
        <yt>{} - {}</yt>
    </div><br>
    <div id="submitForm19">
        <input type="submit" value="{}" name="youtube_id"><br><br>
        <yt>{} - {}</yt>
    </div><br>
    <div id="submitForm20">
        <input type="submit" value="{}" name="youtube_id"><br><br>
        <yt>{} - {}</yt>
    </div><br>
    </form>
</body>
</html>
    """
