import streamlit as st
from PIL import Image

left_column, right_column = st.columns(2)


st.title("クイズ")


st.write("""クイズの説明   """)

questions = ["第1問","第2問","第3問","第4問","第5問","第6問","第7問","第8問","第9問","第10問"]#追加忘れずに
number_of_answer = 0


st.caption("                           ")
st.caption("                           ")
st.caption("                           ")
st.caption(questions[0])
option = st.selectbox('問題文１',
                     ("",'黒', 'ピンク', '白', "赤"))


if option == "白":
    number_of_answer += 1
    answer_0 = "〇"
else :
    answer_0 = "✕"



st.caption("                           ")
st.caption("                           ")
st.caption("                           ")
st.caption(questions[1])
option = st.selectbox('問題文２',
                    
                    ("",'１', '２', '３', "４"))
if option == "１":
    number_of_answer += 1
    answer_1 = "〇"
else :
    answer_1 = "✕"

st.caption("                           ")
st.caption("                           ")
st.caption("                           ")
st.caption(questions[2])
option = st.selectbox('問題文３',
                    
                    ("",'1', '2', '3', "4"))
if option == "4":
    number_of_answer += 1
    answer_2 = "〇"
else :
    answer_2 = "✕"

st.caption("                           ")
st.caption("                           ")
st.caption("                           ")
st.caption(questions[3])
option = st.selectbox('問題文４',
                    
                    ("",'１', '２', '３', "４"))
if option == "１":
    
        number_of_answer += 1
        answer_3 = "〇"
else :
        answer_3 = "✕"

st.caption("                           ")
st.caption("                           ")
st.caption("                           ")
st.caption(questions[4])
option = st.selectbox('問題サンプル１',
                     ("",'1', '2', '3', "4"))


if option == "正解を書く":
    number_of_answer += 1
    answer_4 = "〇"
else :
    answer_4 = "✕"
    
st.caption("                           ")
st.caption("                           ")
st.caption("                           ")
st.caption(questions[5])
option = st.selectbox('問題サンプル２',
                     ("",'1', '2', '3', "4"))


if option == "正解を書く":
    number_of_answer += 1
    answer_5 = "〇"
else :
    answer_5 = "✕"
    
st.caption("                           ")
st.caption("                           ")
st.caption("                           ")
st.caption(questions[6])
option = st.selectbox('問題サンプル３',
                     ("",'1', '2', '3', "4"))


if option == "正解を書く":
    number_of_answer += 1
    answer_6 = "〇"
else :
    answer_6 = "✕"
    
st.caption("                           ")
st.caption("                           ")
st.caption("                           ")
st.caption(questions[7])
option = st.selectbox('問題サンプル４',
                     ("",'1', '2', '3', "4"))


if option == "正解を書く":
    number_of_answer += 1
    answer_7 = "〇"
else :
    answer_7 = "✕"
        
st.caption("                           ")
st.caption("                           ")
st.caption("                           ")
st.caption(questions[8])
option = st.selectbox('問題サンプル５',
                     ("",'1', '2', '3', "4"))


if option == "正解を書く":
    number_of_answer += 1
    answer_8 = "〇"
else :
    answer_8 = "✕"

st.caption("                           ")
st.caption("                           ")
st.caption("                           ")
st.caption(questions[9])
option = st.selectbox('問題サンプル６',
                     ("",'1', '2', '3', "4"))


if option == "正解を書く":
    number_of_answer += 1
    answer_9 = "〇"
else :
    answer_9 = "✕"
        
        
        




st.caption("                           ")
st.caption("                           ")
st.caption("                           ")
result = "結果をみる"


if st.button(result):
    if number_of_answer == len(questions):
        st.caption("                           ")
        st.caption("                           ")
        st.caption("                           ")
        st.caption("結果は、、、")
        st.subheader("全問正解！！おめでとう")
    else:
        
         
        st.caption("                           ")
        st.caption("                           ")
        st.caption("                           ")
        st.write("結果は、、、")
        st.subheader(str(len(questions))+ "問中、"+ str(number_of_answer)+ "問正解！！")
        st.write( str(questions[0])+"：" +str(answer_0) +"　　　　　　　"+ str(questions[5])+"：" +str(answer_5)   )
        st.write( str(questions[1])+"：" +str(answer_1) +"　　　　　　　"+ str(questions[6])+"：" +str(answer_6)   )
        st.write( str(questions[2])+"：" +str(answer_2) +"　　　　　　　"+ str(questions[7])+"：" +str(answer_7)   )
        st.write( str(questions[3])+"：" +str(answer_3) +"　　　　　　　"+ str(questions[8])+"：" +str(answer_8)   )
        st.write( str(questions[4])+"：" +str(answer_4) +"　　　　　　　"+ str(questions[9])+"：" +str(answer_9)   )
    
    


