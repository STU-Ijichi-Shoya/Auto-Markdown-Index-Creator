
import argparse
import os

def checkn(s:str,defaultReturn='\n'):
    if len(s)<=0:
        return defaultReturn
    if s[-1]=='\n':
        if len(s)>=2 and s[-2]=='\r':
                return '\n\r'
        else:
            return '\n'
    return defaultReturn
    
def nremove(s:str):
    if len(s)<=0:
        return s
    if s[-1]=='\n':
        if len(s)>=2 and s[-2]=='\r':
            return s[:-2]
        else:
            return s[:-1]
    else:
        return s

def convert(filename:str):
    with open(filename,encoding="utf-8") as f:
        ## 文脈キュー保存リスト
        content=[]
        ## 重複回避用カウント変数
        count=0
        ## 目次
        indexList=[]
        ## 目次挿入行
        IndexInsrtLine=-1
        ## indexCommentMark
        indexCommentMarkFlag=False
        ## hashtag
        topLevelHashCount=-1
        for line in f.readlines():
            l=nremove(line)
            ## is insert IndexComment?
            if IndexInsrtLine==-1 and "INDEX SCENE" in l:
                content.append("<!-- INDEX SCENE -->")
                content.append("")
                IndexInsrtLine=len(content)
                indexCommentMarkFlag=True
                continue
            elif "INDEX" in l:
                indexCommentMarkFlag=True
                continue
            elif indexCommentMarkFlag and l=='':
                continue
            elif IndexInsrtLine!=-1:
                indexCommentMarkFlag=False
                ## is title?
                hashTagCount=0
                titleName=''
                idx=-1
                for ch in l:                   
                    idx+=1
                    if ch == "#":
                        hashTagCount+=1
                    elif ch in ["\t"," "]:
                        continue                
                    else:
                        break
                titleName=l[idx:]
                if hashTagCount>0:
                    ## create html index id
                    indexID='INDEX-'+titleName.replace(' ','')+str(count)
                    count+=1
                    if len(indexList)==0:
                        topLevelHashCount=hashTagCount-1
                        hashTagCount=1
                    else:
                        hashTagCount-=topLevelHashCount
                        if hashTagCount<=0:
                            hashTagCount=1
                    indexList.append(' '*(2*(hashTagCount-1))+f'- [{titleName}](#{indexID})')
                    content.append(f'<a id=\"{indexID}\" name=\"{titleName}\"></a>')
                    content.append("")
                
            content.append(l)
        if IndexInsrtLine!=-1:
            
            i=0
            idx=IndexInsrtLine
            
            while i<len(indexList) :
                content.insert(idx,indexList[i])
                idx+=1
                i+=1

            content.insert(idx,"")
            content.insert(idx+1,"<!-- INDEX SCENE END -->")
            content.insert(idx+2,"")

        with open(filename,'w',encoding="utf-8") as f:
            print('\n'.join(content),file=f)
        return


def main():

    parser=argparse.ArgumentParser()
    parser.add_argument('-o',"--output",help="指定なしの場合書き換える",type=str)
    parser.add_argument("-d","--inputDirctory",help="markdownが入ったディレクトリを指定する．ここで，-dの指定がない場合，カレントディレクトリを-dに代入する",default=os.getcwd())
    parser.add_argument("-i","--inputFile",help="単一ファイルを変換する,-dを指定している場合，エラーになる",default="")
    args = parser.parse_args()

    print('start')
    if args.inputFile == "":
        if args.inputDirctory=="":
            print("ファイル指定，ディレクトリ指定なし")
            return
        else:
            print("ファイル変換再帰モード")

            for cudir,_,files in os.walk(args.inputDirctory):
                for file in files:
                    if ".md" in file:
                        try:
                            filename=os.path.join(cudir,file)
                            convert(filename)
                            print(file,"ok")
                        except:
                            print(file,'fail')
    else:
        convert(args.inputFile)
        print("単一ファイル変換モード")
    
    

if __name__ == '__main__':
    main()

    