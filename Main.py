import streamlit as st

st.title('화면구현')
st.subheader(':blue[선생님] : 박제현:sunglasses:')
st.subheader('배우는 것 : :rainbow[HTML, CSS, JS]')
st.slider("만족도", 0, 100,90)

학번 = st.text_input('학번을 입력하세요.')
if st.button('학번 저장') :
    if 'stnum' not in st.session_state:
        st.session_state.stnum = 학번
    else :
        st.session_state.stnum = 학번

이름 = st.text_input('이름을 입력하세요.')
if st.button('이름 저장') :
    if 'name' not in st.session_state:
        st.session_state.name = 이름
    else :
        st.session_state.name = 이름
st.title(':red[예제] :red-background[:rainbow[부트스트랩 사용]]')
code = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    <style>
        .container {
            width: 600px;
            border: 1px solid black;
            margin: 0 auto;
            border-radius: 10px;
            padding: 20px 20px;
        }
    </style>

</head>
<body>
    <div class="container">
        <form action="">
            <h1>회원가입 페이지</h1>
            <hr>
            <div class="form-floating mb-3">
                <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
                <label for="floatingInput">Email 주소</label>
            </div>
            <div class="form-floating mb-3">
                <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
                <label for="floatingPassword">비밀번호</label>
            </div>
            <div class="form-floating mb-3">
                <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
                <label for="floatingPassword">비밀번호 확인</label>
            </div>
            <hr>
            <div class="row g-2">
                <div class="col-md">
                <div class="form-floating">
                    <input type="tel" class="form-control" id="floatingInputGrid" placeholder="010-1234-5678">
                    <label for="floatingInputGrid">전화번호</label>
                </div>
                </div>
                <div class="col-md">
                <div class="form-floating">
                    <select class="form-select" id="floatingSelectGrid" aria-label="Floating label select example">
                    <option selected>메뉴를 열어주세요</option>
                    <option value="1">프론트엔드</option>
                    <option value="2">백엔드</option>
                    <option value="3">UX/UI 디자인</option>
                    </select>
                    <label for="floatingSelectGrid">개발 직무</label>
                </div>
                </div>
            </div><br><br>
            <div class="mb-3 form-check">
                <input type="checkbox" class="form-check-input" id="exampleCheck1">
                <label class="form-check-label" for="exampleCheck1">Check me out</label>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</body>
</html>'''