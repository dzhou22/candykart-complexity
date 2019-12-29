from big_ol_pile_of_manim_imports import *

class Reduction(Scene):
    def construct(self):
        title=TextMobject("The Reduction").scale(2)
        self.play(Write(title))
        self.wait(2)
        title2=TextMobject("The Reduction").to_corner(UL)
        self.play(Transform(title,title2))
        suppose=TextMobject(r"Suppose we are given a formula $\varphi$ with $n$ variables and $m$ clauses.").scale(0.75)
        suppose.move_to(2*UP+LEFT)
        self.play(FadeIn(suppose))
        board=TextMobject("We use the gadgets to construct an equivalent gameboard.").scale(0.75)
        board.move_to(UP+1.63*LEFT)
        self.play(FadeIn(board))
        self.wait(2)
        self.play(FadeOut(suppose),FadeOut(board))
        rect=Rectangle(height=1,width=2).move_to(DOWN*1.5)
        rect2=Rectangle(height=1,width=2).move_to(DOWN*0.5)
        rect3=Rectangle(height=1,width=2).move_to(UP*0.5)
        rect4=Rectangle(height=1,width=2).move_to(UP*1.5)
        l1=TextMobject("True").move_to(rect)
        l2=TextMobject("False").move_to(rect2)
        l3=TextMobject(r"$\neg x_i$").move_to(rect3)
        l4=TextMobject(r"$x_i$").move_to(rect4)
        self.play(FadeIn(rect),FadeIn(rect2),FadeIn(rect3),FadeIn(rect4),FadeIn(l1),FadeIn(l2),FadeIn(l3),FadeIn(l4))
        self.wait()
        varRect=Rectangle(height=4,width=1.5).move_to(3*LEFT)
        self.play(ReplacementTransform(rect,varRect),ReplacementTransform(rect2,varRect),ReplacementTransform(rect3,varRect),ReplacementTransform(rect4,varRect),ReplacementTransform(l1,varRect),ReplacementTransform(l2,varRect),ReplacementTransform(l3,varRect),ReplacementTransform(l4,varRect))
        self.wait()
        self.remove(varRect)
        newVarRect=Rectangle(height=4,width=1.5).move_to(3*LEFT)
        self.add(newVarRect)
        varRect2=Rectangle(height=4,width=1.5).move_to(5*LEFT)
        varRect3=Rectangle(height=4,width=1.5).move_to(4*RIGHT)
        dots=TextMobject(r"$\cdots$").scale(3)
        self.play(ReplacementTransform(varRect.copy(),varRect2),ReplacementTransform(varRect,varRect3),Write(dots))
        self.wait()
        varRect4=Rectangle(height=4,width=3).move_to(4*LEFT)
        self.play(ReplacementTransform(newVarRect,varRect4),ReplacementTransform(varRect2,varRect4),ReplacementTransform(varRect3,varRect4),ReplacementTransform(dots,varRect4))
        self.remove(varRect4)
        newVarRect4=Rectangle(height=4,width=3).move_to(4*LEFT)
        self.add(newVarRect4) #variable rectangle
        self.wait()
        cRect=Rectangle(height=2,width=1).move_to(2*UP+RIGHT)
        cRect2=Rectangle(height=2,width=1).move_to(2*RIGHT)
        cRect3=Rectangle(height=2,width=1).move_to(2*DOWN+3*RIGHT)
        self.play(Write(cRect),Write(cRect2),Write(cRect3))
        self.wait()
        wire1=Rectangle(height=0,width=3).move_to(1.5*UP+LEFT)
        wire2=Rectangle(height=0,width=4).move_to(0.5*LEFT)
        wire3=Rectangle(height=0,width=5).move_to(1.5*DOWN)
        self.play(Write(wire1),Write(wire2),Write(wire3))
        self.wait()
        self.remove(newVarRect4)
        self.remove(cRect)
        self.remove(cRect2)
        self.remove(cRect3)
        self.remove(wire1)
        self.remove(wire2)
        self.remove(wire3)
        self.wait()
        dim=TextMobject(r"This board has width $O(n+m)$ and height $O(poly(n+m))$").move_to(0.5*UP)
        dim2=TextMobject(r"so we can construct it in polynomial time.").move_to(0.5*DOWN)
        self.play(Write(dim),Write(dim2))
        self.wait()
        self.play(FadeOut(dim),FadeOut(dim2))
        self.wait()
        text=TextMobject(r"Now pass this gameboard into $CANDYCRUSH$").move_to(0.5*UP)
        text2=TextMobject(r"with $k=n$ and $s$ being the max score achievable.").move_to(0.5*DOWN)
        self.play(Write(text),Write(text2))
        self.wait()
        text3=TextMobject(r"$CANDYCRUSH$ outputs $1$ iff $\varphi$ is satisfiable.").move_to(UP)
        self.play(Transform(text,text3),Transform(text2,text3))
        self.wait()
        conclusion=TextMobject(r"So $3SAT\le_p CANDYCRUSH$.")
        self.play(Write(conclusion))
        self.wait()
        conclusion2=TextMobject(r"Therefore, $CANDYCRUSH$ is $\mathbf{NP}$-hard.").move_to(DOWN)
        self.play(Write(conclusion2))
        self.play(FadeOut(conclusion),FadeOut(conclusion2),FadeOut(title),FadeOut(text),FadeOut(text2))
        self.wait()
        tit=TextMobject("Conclusion").to_corner(UL)
        self.play(FadeIn(tit))
        end=TextMobject(r"We have shown that $CANDYCRUSH\in\mathbf{NP}$").move_to(UP)
        end2=TextMobject(r"and $CANDYCRUSH$ is $\mathbf{NP}$-hard.")
        end3=TextMobject(r"Together, these imply that $CANDYCRUSH$ is $\mathbf{NP}$-complete.").move_to(DOWN)
        self.play(Write(end))
        self.play(Write(end2))
        self.play(Write(end3))
        sq=TextMobject(r"$\blacksquare$").scale(5).to_corner(DR)
        self.wait()
        self.add(sq)
        self.wait()
        self.play(FadeOut(tit),FadeOut(end),FadeOut(end2),FadeOut(end3),FadeOut(sq))
        self.wait()

class Main(Scene):
    def construct(self):
        self.title()
        self.definitions()
        self.np()
        npcomplete=TextMobject("Now we show that $CANDYCRUSH$ is $\mathbf{NP}$-hard.")
        self.play(Write(npcomplete.to_edge(UP)))
        method=TextMobject("We show this by a reduction from $3SAT$.")
        method.to_edge(UP,buff=2.5)
        self.play(Write(method))
        gadgets=TextMobject("We will introduce a series of gadgets").to_edge(UP,buff=3.5)
        gadgets2=TextMobject("that will allow us to convert any $3SAT$ instance").to_edge(UP,buff=4)
        gadgets3=TextMobject("to an instance of $CANDYCRUSH$.").to_edge(UP,buff=4.5)
        self.play(FadeIn(gadgets), FadeIn(gadgets2),FadeIn(gadgets3))
        self.wait(3)
        self.play(FadeOut(gadgets),FadeOut(gadgets2),FadeOut(gadgets3),FadeOut(method))
        gadgets4 = TextMobject("Gadgets").scale(1.5).to_corner(UL)
        self.play(Transform(npcomplete,gadgets4))
        self.background()
        self.truegadget()
        #self.falsegadget()
        self.assignmentneg()
        self.assignmentpos()
        self.wire()
        self.clause()
        title=TextMobject("How do we put it all together?").to_edge(UP).scale(1.5)
        self.play(Transform(npcomplete, title))

    def background(self):
        back=TexMobject(r"""
        \begin{matrix}
        R & O & R & O & R\\
        B & P & B & P & B\\
        R & O & R & O & R\\
        B & P & B & P & B\\
        R & O & R & O & R
        \end{matrix}
        """)
        text=TextMobject("Neutral Background").next_to(back,DOWN,buff=1)
        back2=TexMobject(r"""
        \begin{matrix}
        R & O & R & O & R\\
        B & P &   &   & B\\
        R &   & B & P & R\\
        B & O & R & O & B\\
        R & P & B & P & R
        \end{matrix}
        """)
        back3=TexMobject(r"""
        \begin{matrix}
        R & O & R & O & R\\
        B & P & G & G & B\\
        R & G & B & P & R\\
        B & O & R & O & B\\
        R & P & B & P & R
        \end{matrix}
        """)
        back4=TexMobject(r"""
        \begin{matrix}
        \cdot & \cdot & \cdot & \cdot & \cdot \\
        \cdot & \cdot & \cdot & \cdot & \cdot \\
        \cdot & \cdot & \cdot & \cdot & \cdot \\
        \cdot & \cdot & \cdot & \cdot & \cdot \\
        \cdot & \cdot & \cdot & \cdot & \cdot 
        \end{matrix}
        """)
        self.play(FadeIn(text))
        self.play(FadeIn(back))
        self.wait()
        self.play(FadeOut(back),FadeIn(back2))
        self.wait()
        self.play(FadeOut(back2),FadeIn(back3))
        self.wait()
        self.play(FadeOut(back3),FadeIn(back4))
        self.wait()
        self.play(FadeOut(back4),FadeOut(text))
        self.wait()

    def title(self):
        title=TextMobject("How hard is Candy Crush?").scale(2)
        self.play(Write(title))
        self.wait()
        self.play(LaggedStart(FadeOutAndShiftDown, title))
        answer=TextMobject("Answer: NP-complete").scale(1.5)
        self.play(Write(answer))
        self.wait()
        self.play(FadeOut(answer))

    def definitions(self):
        grid = NumberPlane()
        grid_title = TextMobject("Candy Crush is played on a grid").move_to(0.5*UP)
        grid_title.scale(1.5)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeInFromDown(grid_title),
            Write(grid), run_time=2.5
        )
        self.wait()
        dimensions=TexMobject(r"\text{Call the dimensions } w \times h").scale(1.5)
        dimensions.move_to(0.5*DOWN)
        self.play(Transform(grid_title, dimensions))
        self.wait(2)
        self.remove(grid,grid_title)
        text=TextMobject("Each square is filled with one of six different colored candies")
        arr=TextMobject("R", "O", "Y", "G", "B", "P")
        arr2=TextMobject("R", "O", "G", "Y", "B", "P")
        arr.move_to(DOWN*1.5)
        arr[0].set_color(RED)
        arr[1].set_color(ORANGE)
        arr[2].set_color("#FFFF00")
        arr[3].set_color("00FF00")
        arr[4].set_color(BLUE)
        arr[5].set_color("DC28E2")
        arr2.move_to(DOWN*1.5)
        arr2[0].set_color(RED)
        arr2[1].set_color(ORANGE)
        arr2[3].set_color("#FFFF00")
        arr2[2].set_color("00FF00")
        arr2[4].set_color(BLUE)
        arr2[5].set_color("DC28E2")
        self.play(FadeIn(text))
        self.play(Write(arr))
        self.wait(1.5)
        self.play(FadeOut(text))
        text2=TextMobject("Each square is filled with one of six different colored candies")
        text3=TextMobject("A player may swap two candies in neighboring squares")
        text4=TextMobject("When a player forms a chain of 3 identical candies or more, the identical")
        text5=TextMobject("candies are deleted and new ones fall from above and take their place.")
        text6=TextMobject("The player's final score is equal to the number of chains deleted.")
        text7=TextMobject("Define the $CANDYCRUSH$ problem as follows:")
        problem=TextMobject("Given a gameboard and a number $k$ swaps, is a score $s$ achievable?")
        self.play(FadeIn(text3))
        self.play(Transform(arr,arr2))
        self.wait(2)
        self.play(FadeOut(text3))
        self.play(FadeOut(arr))
        self.play(FadeIn(text4.scale(0.75).move_to(0.25*UP)),FadeIn(text5.scale(0.75).move_to(0.25*DOWN)))
        self.wait(2)
        self.play(FadeOut(text4),FadeOut(text5))
        self.play(FadeIn(text6))
        self.wait(2)
        self.play(FadeOut(text6))
        self.play(FadeIn(text7))
        self.wait(2)
        self.play(FadeOut(text7))
        self.play(FadeIn(problem.scale(0.85)))
        self.wait(3)
        self.play(FadeOut(problem))
        
    def np(self):
        text=TextMobject("First we show that $CANDYCRUSH\in\mathbf{NP}.$")
        text.to_edge(UP)
        self.play(Write(text))
        text2=TextMobject("Given a sequence of moves, we can just play the game")
        text3=TextMobject("then check if the final score is large enough.")
        text2.to_edge(UP,buff=2)
        text3.to_edge(UP,buff=2.5)
        self.play(FadeIn(text2), FadeIn(text3))
        self.wait()
        text4=TextMobject("Each move takes constant time.")
        text5=TextMobject("Comparing the final score can be done digit by digit")
        text6=TextMobject("in $O(\log n)$ time.")
        text4.to_edge(UP,buff=3.5)
        text5.to_edge(UP,buff=4.5)
        text6.to_edge(UP,buff=5)
        self.play(FadeIn(text4))
        self.wait()
        self.play(FadeIn(text5), FadeIn(text6))
        self.wait(2)
        text7=TextMobject("Then overall, the $CANDYCRUSH$ problem is checkable in polynomial time.")
        text7.to_edge(DOWN,buff=1.5).scale(0.75)
        self.play(FadeIn(text7))
        self.wait(2)
        self.play(FadeOut(text),FadeOut(text2),FadeOut(text3),FadeOut(text4),FadeOut(text5),FadeOut(text6))
        self.play(FadeOut(text7))
        self.wait()

    def clause(self):
        title=TextMobject("Clause")
        subtitle=TexMobject(r"""
        \text{``anything such that the 4th column drops}\\
        \text{only on a satisfying assignment''}\hspace{7mm}
        """)
        #subtitle.to_edge(UP,buff=4)
        self.play(Write(title))
        self.wait()
        self.play(Transform(title,subtitle))
        self.wait()
        example=TexMobject(r"\text{For example: } \neg x_1 \vee x_2")
        example.to_edge(UP,buff=0.5)
        self.play(Transform(title,example))
        self.wait()
        matrix=TexMobject(r"""
        \begin{matrix}
          & G & G & \cdot & \cdot \\
        \neg x_2  & \cdot & \cdot & \cdot & \cdot \\
          & \cdot & \cdot & \cdot & \cdot \\
          & \cdot & G & \cdot & \cdot \\
          & \cdot & \cdot & \cdot & \cdot \\
          & \cdot & \cdot & G & G \\
          & \cdot & \cdot & \cdot & \cdot \\
          & G & G & \cdot & \cdot \\
        x_2  & \cdot & \cdot & \cdot & \cdot \\
          & \cdot & \cdot & \cdot & \cdot \\
          & \cdot & \cdot & \cdot & \cdot \\
        x_1  & G & G & \cdot & \cdot \\
          & \cdot & \cdot & \cdot & \cdot \\
          & \cdot & G & \cdot & \cdot \\
          & \cdot & \cdot & G & G \\
          & \cdot & \cdot & \cdot & \cdot \\
        \neg x_1  & G & G & \cdot & \cdot \\
        \end{matrix}
        """)
        matrix.scale(0.5)
        self.play(Write(matrix))
        self.wait()
        plus=TexMobject(r"+")
        matrix2=TexMobject(r"""
        \begin{matrix}
        G & \cdot & \cdot \\
        \cdot & G & G
        \end{matrix}
        """)
        plus.move_to(2*RIGHT)
        matrix2.move_to(4*RIGHT)
        timesn=TexMobject(r"\bigg(\hspace{18mm}\bigg)\times N")
        timesn.move_to(4.7*RIGHT)
        self.play(Write(plus))
        self.play(Write(matrix2),Write(timesn))
        self.wait()
        rect=Rectangle(height=2,width=2)
        rect.move_to(6*RIGHT+2*DOWN)
        self.play(Transform(matrix,rect),Transform(matrix2,rect),Transform(plus,rect),Transform(timesn,rect),Transform(title,rect),)
        self.play(Write(TextMobject("clause").move_to(6*RIGHT+2*DOWN)))
        self.wait()


    def wire(self):
        label=TextMobject("wire")
        label2=TextMobject("wire")
        row1_1=TexMobject(r"""
        \begin{matrix}
        \cdot \\
        \cdot  \\ 
        G  \\
        \cdot  \\
        \cdot  \\
        \cdot  \\
        G 
        \end{matrix}
        """)
        row1_2=TexMobject(r"""
        \begin{matrix}
        \cdot \\
        \cdot  \\ 
        \cdot  \\
        G  \\
        \cdot  \\
        \cdot  \\
        \cdot 
        \end{matrix}
        """)
        row1_3=TexMobject(r"""
        \begin{matrix}
        \cdot \\
        \cdot  \\ 
        \cdot  \\
        \cdot  \\
        \cdot  \\
        \cdot  \\
        \cdot 
        \end{matrix}
        """)
        row1_1.move_to(LEFT)
        row1_2.move_to(LEFT)
        row1_3.move_to(LEFT)
        row2_1=TexMobject(r"""
        \begin{matrix}
        \cdot \\
        \cdot  \\ 
        G  \\
        \cdot  \\
        \cdot  \\
        \cdot  \\
        G 
        \end{matrix}
        """)
        row2_2=TexMobject(r"""
        \begin{matrix}
        \cdot \\
        \cdot  \\ 
        \cdot  \\
        G  \\
        \cdot  \\
        \cdot  \\
        \cdot 
        \end{matrix}
        """)
        row2_3=TexMobject(r"""
        \begin{matrix}
        \cdot \\
        \cdot  \\ 
        \cdot  \\
        \cdot  \\
        \cdot  \\
        \cdot  \\
        \cdot 
        \end{matrix}
        """)
        row3_1=TexMobject(r"""
        \begin{matrix}
        G \\
        out  \\ 
        \cdot  \\
        G  \\
        \cdot  \\
        \cdot  \\
        \cdot 
        \end{matrix}
        """)
        row3_3=TexMobject(r"""
        \begin{matrix}
        \cdot \\
        G  \\ 
        \cdot  \\
        \cdot \\
        \cdot  \\
        \cdot  \\
        \cdot 
        \end{matrix}
        """)
        row3_1.move_to(RIGHT+0.1*UP)
        row3_3.move_to(RIGHT)
        rect = Rectangle(height=0,width=2)
        rect.move_to(3.5*LEFT+2.25*DOWN)
        label2.move_to(3.5*LEFT+2.75*DOWN)
        label.next_to(row2_1,DOWN,buff=0.5)
        self.play(Write(label))
        self.wait()
        self.play(FadeInFrom(row1_1, DOWN),FadeInFrom(row2_1, DOWN),FadeInFrom(row3_1, DOWN))
        self.wait()
        self.play(Transform(row1_1,row1_2),Transform(row2_1,row2_2))
        self.wait()
        self.play(Transform(row1_1,row1_3),Transform(row2_1,row2_3),Transform(row3_1,row3_3))
        self.wait()
        self.play(Transform(label,label2),Transform(row1_1,rect),Transform(row2_1,rect),Transform(row3_1,rect))
        self.wait()
        
    def assignmentpos(self):
        label=TexMobject("x_i")
        label2=TexMobject("x_i")
        row1_1=TexMobject(r"""
        \begin{matrix}
        \cdot \\
        \cdot  \\ 
        \cdot  \\
        \cdot  \\
        \cdot  \\
        G  \\
        \cdot 
        \end{matrix}
        """)
        row1_3=TexMobject(r"""
        \begin{matrix}
        \cdot \\
        \cdot  \\ 
        \cdot  \\
        \cdot  \\
        \cdot  \\
        \cdot  \\
        \cdot 
        \end{matrix}
        """)
        row1_1.move_to(LEFT)
        row1_3.move_to(LEFT)
        row2_1=TexMobject(r"""
        \begin{matrix}
        \cdot \\
        \cdot\\ 
        \cdot \\
        \cdot \\
        \cdot \\
        G \\
        \cdot 
        \end{matrix}
        """)
        row2_3=TexMobject(r"""
        \begin{matrix}
        \cdot \\
        \cdot\\ 
        \cdot \\
        \cdot \\
        \cdot \\
        \cdot \\
        \cdot 
        \end{matrix}
        """)
        row3_1= TexMobject(r"""
        \begin{matrix}
        G \\
        \cdot \\ 
        G \\
        \cdot \\
        out \\
        \cdot \\
        \cdot
        \end{matrix}
        """)
        row3_2= TexMobject(r"""
        \begin{matrix}
        \cdot \\
        \cdot \\ 
        \cdot \\
        G \\
        out \\
        G \\
        \cdot
        \end{matrix}
        """)
        row3_3= TexMobject(r"""
        \begin{matrix}
        \cdot \\
        \cdot \\ 
        \cdot \\
        \cdot \\
        G \\
        \cdot \\
        \cdot
        \end{matrix}
        """)
        row3_1.move_to(RIGHT+0.1*UP)
        row3_2.move_to(RIGHT)
        row3_3.move_to(RIGHT)
        rect=Rectangle(height=1,width=2)
        rect.move_to(6*LEFT+0.5*UP)
        label2.move_to(6*LEFT+0.5*UP)
        label.next_to(row2_1,DOWN,buff=0.5)
        self.play(Write(label))
        self.play(FadeInFrom(row1_1, DOWN),FadeInFrom(row2_1, DOWN),FadeInFrom(row3_1, DOWN))
        self.wait()
        self.play(Transform(row3_1,row3_2))
        self.wait()
        self.play(Transform(row1_1, row1_3),Transform(row2_1, row2_3),Transform(row3_1, row3_3))
        self.wait()
        self.play(Transform(row1_1,rect),Transform(row2_1,rect),Transform(row3_1,rect),Transform(label,label2))
        self.wait()

    def assignmentneg(self):
        label=TexMobject("\\neg x_i")
        label2=TexMobject("\\neg x_i")
        row1_1=TexMobject(r"""
        \begin{matrix}
        \cdot  \\ 
        \cdot  \\
        \cdot  \\
        \cdot  \\
        G  \\
        \cdot 
        \end{matrix}
        """)
        row1_3=TexMobject(r"""
        \begin{matrix}
        \cdot  \\ 
        \cdot  \\
        \cdot  \\
        \cdot  \\
        \cdot  \\
        \cdot 
        \end{matrix}
        """)
        row1_1.move_to(LEFT)
        row1_3.move_to(LEFT)
        row2_1=TexMobject(r"""
        \begin{matrix}
        \cdot\\ 
        G \\
        \cdot \\
        \cdot \\
        \cdot \\
        \cdot 
        \end{matrix}
        """)
        row2_2=TexMobject(r"""
        \begin{matrix}
        \cdot\\ 
        \cdot \\
        \cdot \\
        \cdot \\
        G \\
        \cdot 
        \end{matrix}
        """)
        row2_3=TexMobject(r"""
        \begin{matrix}
        \cdot\\ 
        \cdot \\
        \cdot \\
        \cdot \\
        \cdot \\
        \cdot 
        \end{matrix}
        """)
        row3_1= TexMobject(r"""
        \begin{matrix}
        G \\ 
        out \\
        \cdot \\
        \cdot \\
        G \\
        \cdot
        \end{matrix}
        """)
        row3_3= TexMobject(r"""
        \begin{matrix}
        \cdot \\ 
        G \\
        \cdot \\
        \cdot \\
        \cdot \\
        \cdot
        \end{matrix}
        """)
        row3_1.move_to(RIGHT+0.1*UP)
        row3_3.move_to(RIGHT)
        rect=Rectangle(height=1,width=2)
        rect.move_to(6*LEFT+0.5*DOWN)
        label2.move_to(6*LEFT+0.5*DOWN)
        label.next_to(row2_2,DOWN,buff=0.5)
        self.play(Write(label))
        self.play(FadeInFrom(row1_1, DOWN),FadeInFrom(row2_1, DOWN),FadeInFrom(row3_1, DOWN))
        self.wait()
        self.play(Transform(row2_1,row2_2))
        self.wait()
        self.play(Transform(row1_1, row1_3),Transform(row2_1, row2_3),Transform(row3_1, row3_3))
        self.wait()
        self.play(Transform(row1_1,rect),Transform(row2_1,rect),Transform(row3_1,rect),Transform(label,label2))
        self.wait()


    def truegadget(self):
        title=TextMobject("True")
        title2=TextMobject("True")
        row1_1=TexMobject(r"""
        \begin{matrix}
        \cdot \\ 
        \cdot \\
        \cdot \\
        \cdot 
        \end{matrix}
        """)
        row1_1.move_to(LEFT)
        row2_1=TexMobject(r"""
        \begin{matrix}
        \cdot\\ 
        \cdot\\
        G  \\
        G
        \end{matrix}
        """)
        row2_1.move_to(0.05*DOWN)
        row3_1=TexMobject(r"""
        \begin{matrix}
        G \\ 
        G \\
        \cdot \\
        \cdot
        \end{matrix}
        """)
        row3_1.move_to(RIGHT+0.1*UP)
        row2_2=TexMobject(r"""
        \begin{matrix} 
        \cdot \\ 
        \cdot \\
        \cdot \\
        G 
        \end{matrix}
        """)
        row2_2.move_to(0.05*DOWN)
        row3_2 = TexMobject(r"""
        \begin{matrix} 
        G \\ 
        G \\
        G \\
        \cdot
        \end{matrix}
        """)
        row3_2.move_to(RIGHT+0.1*UP)
        row2_3=TexMobject(r"""
        \begin{matrix} 
        \cdot\\
        \cdot \\
        \cdot \\
        G 
        \end{matrix}
        """)
        row2_3.move_to(0.05*DOWN)
        row3_3 = TexMobject(r"""
        \begin{matrix} 
        \cdot \\ 
        \cdot \\
        \cdot \\
        \cdot
        \end{matrix}
        """)
        row3_3.move_to(RIGHT)
        square=Rectangle(height=1,width=2)
        square.move_to(6*LEFT+2.5*DOWN)
        title2.move_to(6*LEFT+2.5*DOWN)
        title.next_to(row2_1,DOWN,buff=0.5)
        self.play(Write(title),FadeInFrom(row1_1, UP),FadeInFrom(row2_1, UP),FadeInFrom(row3_1, UP))
        self.wait()
        self.play(Transform(row2_1,row2_2),Transform(row3_1,row3_2))
        self.wait()
        self.play(Transform(row2_1,row2_3),Transform(row3_1,row3_3))
        self.wait()
        self.play(Transform(row1_1,square),Transform(row2_1,square),Transform(row3_1,square),Transform(title,title2))
        self.wait() 
        self.falsegadget()
    
    def falsegadget(self):
        title=TextMobject("False")
        title2=TextMobject("False")
        row1_1=TexMobject(r"""
        \begin{matrix}
        \cdot \\ 
        \cdot \\
        \cdot \\
        \cdot 
        \end{matrix}
        """)
        row1_1.move_to(LEFT)
        row2_1=TexMobject(r"""
        \begin{matrix}
        \cdot\\ 
        \cdot\\
        G  \\
        G
        \end{matrix}
        """)
        row3_1=TexMobject(r"""
        \begin{matrix}
        G \\ 
        G \\
        \cdot \\
        \cdot
        \end{matrix}
        """)
        row3_1.move_to(RIGHT+0.1*UP)
        row2_2=TexMobject(r"""
        \begin{matrix} 
        \cdot \\ 
        G \\
        G \\
        G 
        \end{matrix}
        """)
        row3_2 = TexMobject(r"""
        \begin{matrix} 
        G \\ 
        \cdot \\
        \cdot \\
        \cdot
        \end{matrix}
        """)
        row3_2.move_to(RIGHT+0.1*UP)
        row2_3=TexMobject(r"""
        \begin{matrix} 
        \cdot\\
        \cdot \\
        \cdot \\
        \cdot 
        \end{matrix}
        """)
        row3_3 = TexMobject(r"""
        \begin{matrix} 
        G \\ 
        \cdot \\
        \cdot \\
        \cdot
        \end{matrix}
        """)
        row3_3.move_to(RIGHT+0.1*UP)
        square=Rectangle(height=1,width=2)
        square.move_to(6*LEFT+1.5*DOWN)
        title2.move_to(6*LEFT+1.5*DOWN)
        title.next_to(row2_1,DOWN,buff=0.5)
        self.play(Write(title),FadeInFrom(row1_1, UP),FadeInFrom(row2_1, UP),FadeInFrom(row3_1, UP))
        self.wait()
        self.play(Transform(row2_1,row2_2),Transform(row3_1,row3_2))
        self.wait()
        self.play(Transform(row2_1,row2_3),Transform(row3_1,row3_3))
        self.wait()
        self.play(Transform(row1_1,square),Transform(row2_1,square),Transform(row3_1,square),Transform(title,title2))
        self.wait() 

class TrueGadget(Scene):
    def construct(self):
        title=TextMobject("True")
        title2=TextMobject("True")
        matrix1 = TexMobject(r"""
        \begin{matrix}
        \cdot & \cdot & G \\ 
        \cdot & \cdot & G \\
        \cdot & G & \cdot \\
        \cdot & G & \cdot
        \end{matrix}
        """)
        matrix2 = TexMobject(r"""
        \begin{matrix} 
        \cdot & \cdot & G \\ 
        \cdot & \cdot & G \\
        \cdot & \cdot & G \\
        \cdot & G & \cdot
        \end{matrix}
        """)
        matrix3 = TexMobject(r"""
        \begin{matrix} 
        \cdot & \cdot & \cdot \\ 
        \cdot & \cdot & \cdot \\
        \cdot & \cdot & \cdot \\
        \cdot & G & \cdot
        \end{matrix}
        """)
        square=Square()
        square.move_to(6*LEFT+2.5*UP)
        title2.move_to(6*LEFT+2.5*UP)
        title.next_to(matrix1,DOWN,buff=0.5)
        self.play(Write(title),FadeInFrom(matrix1, UP))
        self.wait()
        self.play(Transform(matrix1,matrix2))
        self.wait()
        self.play(Transform(matrix1, matrix3))
        self.wait()
        self.play(Transform(matrix1,square),Transform(title,title2))
        self.wait()
        
class FalseGadget(Scene):
    def construct(self):
        title=TextMobject("False")
        title2=TextMobject("False")
        matrix1 = TexMobject(r"""
        \begin{matrix}
        \cdot & \cdot & G \\ 
        \cdot & \cdot & G \\
        \cdot & G & \cdot \\
        \cdot & G & \cdot
        \end{matrix}
        """)
        matrix2 = TexMobject(r"""
        \begin{matrix} 
        \cdot & \cdot & G \\ 
        \cdot & G & \cdot \\
        \cdot & G & \cdot \\
        \cdot & G & \cdot
        \end{matrix}
        """)
        matrix3 = TexMobject(r"""
        \begin{matrix} 
        \cdot & \cdot & G \\ 
        \cdot & \cdot & \cdot \\
        \cdot & \cdot & \cdot \\
        \cdot & \cdot & \cdot
        \end{matrix}
        """)
        square=Square()
        square.move_to(6*LEFT+1.5*DOWN)
        title2.move_to(6*LEFT+1.5*DOWN)
        title.next_to(matrix1,DOWN,buff=0.5)
        self.play(Write(title),FadeInFrom(matrix1, UP))
        self.wait()
        self.play(Transform(matrix1,matrix2))
        self.wait()
        self.play(Transform(matrix1, matrix3))
        self.wait()
        self.play(Transform(matrix1,square),Transform(title,title2))
        self.wait()
        
