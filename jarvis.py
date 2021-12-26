import pyttsx3
import pywhatkit as kit
engine = pyttsx3.init()

rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 165)     # setting up new voice rate

print('hello sir my name is jarvis')
engine.say('hello sir my name is jarvis')
engine.runAndWait()
print('please tell how can i help you')
engine.say('please tell how can i help you')
engine.runAndWait()
print('but before that')
engine.say('but before that')
engine.runAndWait()
engine.say('enter your name sir')
engine.runAndWait()
name = input('enter your name sir: ')
engine.say(f'enter what you want{name}')
engine.runAndWait()
what = input(f'enter what you want {name}(math,message,video,search,info,drawing): ')

if 'math' in what:
    mathwatt = input('enter the funcition which you want in  math: ')
    if 'square' in mathwatt:
        sq = int(input('enter the number for square: '))
        s1 = sq * sq
        print(f'square = {s1}')

    elif 'cube' in mathwatt:
        cu = int(input('enter the number for cube:'))
        c1 = cu * cu * cu
        print(f'cube = {c1}')

    elif 'area' in mathwatt:
        l = int(input('enter the length: '))
        b = int(input('enter the breadth: '))
        area = l * b
        print(f'area = {area}')

    elif 'si' in mathwatt:
        p = int(input('enter the principle:'))
        r = int(input('enter the rate: '))
        t = int(input('enter the time: '))
        si = p * r * t / 100
        print(f'si = {si}')

    elif 'speed' in mathwatt:
        d = int(input('enter the distance(in km): '))
        t = int(input('enter the time(in hour): '))
        speed = d * t
        print(f'speed = {speed}')

    elif 'add' in mathwatt:
        a1 = int(input('enter the 1st number: '))
        a2 = int(input('enter the 2nd number: '))
        add = a1 + a2
        print(f'add ={add}')

    elif 'mul' in mathwatt:
        m1 = int(input('enter the 1st number: '))
        m2 = int(input('enter the 2nd number: '))
        mul = m1 * m2
        print(f'mul = {mul}')

    elif 'div' in mathwatt:
        d1 = int(input('enter the 1st number: '))
        d2 = int(input('enter the 2nd number: '))
        div = d1 / d2
        print(f'div = {div}')

    elif 'sub' in mathwatt:
        s1 = int(input('enter the 1st number: '))
        s2 = int(input('enter the 2nd number: '))
        sub = s1 - s2
        print(f'sub = {sub}')

    elif 'mod' in mathwatt:
        md1 = int(input('enter the 1st number: '))
        md2 = int(input('enter the 2nd number: '))
        mod = md1 % md2
        print(f'mod = {mod}')

    elif 'table' in mathwatt:
        tab = int(input('enter a number for table: '))
        for i in range (0,tab * 11,tab):
            print(f'{tab} x {0+1} = {i}')


elif 'search' in what :
    engine.say('enter what you want search about on google')
    gs = input('enter what you want search about on google')
    kit.search(gs)

elif 'info' in what :
    engine.say('enter what you want to fetch information about topic')
    engine.runAndWait()
    ia = input('enter what you want to fetch information about topic: ')
    kit.info(ia)

elif 'video' in what :
    engine.say('enter the name of the video')
    engine.runAndWait()
    ys = input('enter the name of video: ')
    kit.playonyt(ys)

elif 'message' in what :
    num_name = input('enter the name of people list(harsh bhaya,harsh,pranav sir,sonu bhaya,papa,mom): ')

    if 'harsh bhaya' in num_name:
        message = input('enter your meassage')
        h = int(input('enter the time to send the meassage(in 24 hours format)e): '))
        m = int(input('enter the time to send the meassage(in 60 minutes): '))

        kit.sendwhatmsg(f"+91{9875517479}",f"{message}",h,m)

    elif 'harsh' in num_name:
            message1 = input('enter your meassage')
            h1 = int(input('enter the time to send the meassage(in 24 hours format)e): '))
            m1 = int(input('enter the time to send the meassage(in 60 minutes): '))

            kit.sendwhatmsg(f"+91{ 8769852945}", f"{message1}", h1, m1)

    elif 'pranav sir' in num_name:
            message2 = input('enter your meassage')
            h2 = int(input('enter the time to send the meassage(in 24 hours format): '))
            m2 = int(input('enter the time to send the meassage(in 60 minutes): '))

            kit.sendwhatmsg(f"+91{ 6393228937}", f"{message2}", h2, m2)

    elif 'papa' in num_name:
            message3 = input('enter your meassage')
            h3 = int(input('enter the time to send the meassage(in 24 hours format)e): '))
            m3 = int(input('enter the time to send the meassage(in 60 minutes): '))

            kit.sendwhatmsg(f"+91{ 9005410111}", f"{message3}", h3, m3)

    elif 'mom' in num_name:
            message4 = input('enter your meassage')
            h4 = int(input('enter the time to send the meassage(in 24 hours format)e): '))
            m4 = int(input('enter the time to send the meassage(in 60 minutes): '))

            kit.sendwhatmsg(f"+91{ 8423873971}", f"{message4}", h4, m4)

    elif 'sonu bhaya' in num_name:
            messagm5 = input('enter your meassage')
            m5 = int(input('enter the time to send the meassage(in 24 hours format)e): '))
            m5 = int(input('enter the time to send the meassage(in 60 minutes): '))

            kit.sendwhatmsg(f"+91{ 7977540799}", f"{messagm5}", m5, m5)

    elif 'drawing' in what:
        draw = input("enter your 1st line to convert it into png: ")
        draw2 = input("enter your 2st line to convert it into png: ")
        draw3 = input("enter your 3st line to convert it into png: ")
        png = input('enter the name of png to save it: ')
        kit.text_to_handwriting(f"{draw}\n{draw2}\n{draw3}","c:/users/pc/desktop/meee.png")

yorn = input('do yo want to use this program one more: ')

if 'yes' in yorn:
    fun = input('which program do you want to use:')
    if 'math' in fun:
        mathwatt1 = input('enter the funcition which you want in  math(table,square,cube,area,si,speed,add,mul,div,sub,mod): ')
        if 'square' in mathwatt1:
            sq = int(input('enter the number for square: '))
            s1 = sq * sq
            print(f'square = {s1}')

        elif 'cube' in mathwatt1:
            cu = int(input('enter the number for cube:'))
            c1 = cu * cu * cu
            print(f'cube = {c1}')

        elif 'area' in mathwatt1:
            l = int(input('enter the length: '))
            b = int(input('enter the breadth: '))
            area = l * b
            print(f'area = {area}')

        elif 'si' in mathwatt1:
            p = int(input('enter the principle:'))
            r = int(input('enter the rate: '))
            t = int(input('enter the time: '))
            si = p * r * t / 100
            print(f'si = {si}')

        elif 'speed' in mathwatt1:
            d = int(input('enter the distance(in km): '))
            t = int(input('enter the time(in hour): '))
            speed = d * t
            print(f'speed = {speed}')

        elif 'add' in mathwatt1:
            a1 = int(input('enter the 1st number: '))
            a2 = int(input('enter the 2nd number: '))
            add = a1 + a2
            print(f'add ={add}')

        elif 'mul' in mathwatt1:
            m1 = int(input('enter the 1st number: '))
            m2 = int(input('enter the 2nd number: '))
            mul = m1 * m2
            print(f'mul = {mul}')

        elif 'div' in mathwatt1:
            d1 = int(input('enter the 1st number: '))
            d2 = int(input('enter the 2nd number: '))
            div = d1 / d2
            print(f'div = {div}')

        elif 'sub' in mathwatt1:
            s1 = int(input('enter the 1st number: '))
            s2 = int(input('enter the 2nd number: '))
            sub = s1 - s2
            print(f'sub = {sub}')

        elif 'mod' in mathwatt1:
            md1 = int(input('enter the 1st number: '))
            md2 = int(input('enter the 2nd number: '))
            mod = md1 % md2
            print(f'mod = {mod}')

        elif 'table' in mathwatt1:
            tab = int(input('enter a number for table: '))
            for i in range(0, tab * 11, tab):
                print(f'{tab} x {0 + 1} = {i}')

        else:
            print('this function is not avaliable')


    elif 'search' in fun:
        engine.say('enter what you want search about on google')
        gs = input('enter what you want search about on google: ')
        kit.search(gs)

    elif 'info' in fun:
        engine.say('enter what you want to fetch information about topic')
        engine.runAndWait()
        ia = input('enter what you want to fetch information about topic: ')
        kit.info(ia)

    elif 'video' in fun:
        engine.say('enter the name of the video')
        engine.runAndWait()
        ys = input('enter the name of video: ')
        kit.playonyt(ys)

    elif 'message' in fun:
        num_name = input('enter the name of people list(harsh bhaya,harsh,pranav sir,sonu bhaya,papa,mom): ')

        if 'harsh bhaya' in num_name:
            message = input('enter your meassage')
            h = int(input('enter the time to send the meassage(in 24 hours format)): '))
            m = int(input('enter the time to send the meassage(in 60 minutes): '))

            kit.sendwhatmsg(f"+91{9875517479}", f"{message}", h, m)

        elif 'harsh' in num_name:
            message1 = input('enter your meassage')
            h1 = int(input('enter the time to send the meassage(in 24 hours format)e): '))
            m1 = int(input('enter the time to send the meassage(in 60 minutes): '))

            kit.sendwhatmsg(f"+91{8769852945}", f"{message1}", h1, m1)

        elif 'pranav sir' in num_name:
            message2 = input('enter your meassage')
            h2 = int(input('enter the time to send the meassage(in 24 hours format): '))
            m2 = int(input('enter the time to send the meassage(in 60 minutes): '))

            kit.sendwhatmsg(f"+91{6393228937}", f"{message2}", h2, m2)

        elif 'papa' in num_name:
            message3 = input('enter your meassage')
            h3 = int(input('enter the time to send the meassage(in 24 hours format)e): '))
            m3 = int(input('enter the time to send the meassage(in 60 minutes): '))

            kit.sendwhatmsg(f"+91{9005410111}", f"{message3}", h3, m3)

        elif 'mom' in num_name:
            message4 = input('enter your meassage')
            h4 = int(input('enter the time to send the meassage(in 24 hours format)e): '))
            m4 = int(input('enter the time to send the meassage(in 60 minutes): '))

            kit.sendwhatmsg(f"+91{8423873971}", f"{message4}", h4, m4)

        elif 'sonu bhaya' in num_name:
            messagm5 = input('enter your meassage')
            m5 = int(input('enter the time to send the meassage(in 24 hours format)e): '))
            m5 = int(input('enter the time to send the meassage(in 60 minutes): '))

            kit.sendwhatmsg(f"+91{7977540799}", f"{messagm5}", m5, m5)

        elif 'drawing' in fun:
            draw = input("enter your 1st line to convert it into png: ")
            draw2 = input("enter your 2st line to convert it into png: ")
            draw3 = input("enter your 3st line to convert it into png: ")
            png = input('enter the name of png to save it: ')
            kit.text_to_handwriting(f"{draw}\n{draw2}\n{draw3}", "c:/users/pc/desktop/meee.png")

elif 'no' in yorn:
    print('thanks for choosing me by by')
    engine.say('thanks for choosing me by by')
