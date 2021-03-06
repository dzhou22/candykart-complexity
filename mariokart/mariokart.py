from big_ol_pile_of_manim_imports import *

class Reduction(Scene):
    def construct(self):
        title=TextMobject("The Reduction").scale(2)
        self.play(Write(title))
        self.wait()
        red=TextMobject(r"$QSAT\leq_p MARIOKART$").to_corner(UL)
        self.play(Transform(title,red))
        self.wait()
        setup=TextMobject("2 players: U, E (each has its own track, U's is slightly longer)").move_to(.74*LEFT+2*UP).scale(0.75)
        self.play(FadeIn(setup))
        self.wait()
        stage1=TextMobject("Stage 1: variable assignment").move_to(3.43*LEFT+UP).scale(0.75)
        self.play(FadeIn(stage1))
        self.wait()
        stage2=TextMobject("Stage 1.5: clearing items").move_to(3.75*LEFT).scale(0.75)
        self.play(FadeIn(stage2))
        self.wait()
        stage3=TextMobject("Stage 2: clauses").move_to(4.45*LEFT+DOWN).scale(0.75)
        self.play(FadeIn(stage3))
        self.wait()
        self.play(FadeOut(title),FadeOut(setup),FadeOut(stage1),FadeOut(stage2),FadeOut(stage3))
        self.wait()
        clause=TextMobject("Clauses").to_corner(UL)
        self.play(FadeIn(clause))
        self.clause()
        self.wait()
        variable=TextMobject("Variables").to_corner(UL)
        self.play(Transform(clause,variable))
        self.wait()
        self.variable()
        self.wait()
        clear=TextMobject("Clear").to_corner(UL)
        self.play(Transform(clause,clear))
        self.wait()
        self.clear()
        self.wait()
        self.play(FadeOut(clause))
        self.wait()
        self.restrictions()
        self.wait()
        conclusion=TextMobject("Conclusion").to_corner(UL)
        self.play(FadeIn(conclusion))
        self.wait()
        self.polynomial()
        self.wait()
        self.play(FadeOut(conclusion))
        self.wait()
        end=TextMobject(r"We have shown that $QSAT\leq_p MARIOKART$.")
        end2=TextMobject(r"Hence, $MARIOKART$ is $\mathbf{PSPACE}$-hard.")
        self.play(FadeIn(end))
        self.wait()
        self.play(Transform(end,end2))
        self.wait()
        sq=TextMobject(r"$\blacksquare$").to_corner(DR).scale(4)
        self.add(sq)
        self.wait(6)
    
    def polynomial(self):
        exp1=TextMobject(r"Each gadget has a constant size, so altogether, they can be made in $O(n)$ time").move_to(UP).scale(0.5)
        exp2=TextMobject("Connecting the gadgets takes at most linear time").move_to(0.5*UP).scale(0.5)
        exp3=TextMobject("Tweaking the path so that the universal player's path is slightly longer takes at most polynomial time").move_to(0.25*DOWN).scale(0.5)
        concl=TextMobject("Overall, the reduction can be done in polynomial time").move_to(1.25*DOWN).scale(0.75)
        self.play(FadeIn(exp1))
        self.wait()
        self.play(FadeIn(exp2))
        self.wait()
        self.play(FadeIn(exp3))
        self.wait()
        self.play(FadeIn(concl))
        self.wait()
        self.play(FadeOut(exp1),FadeOut(exp2),FadeOut(exp3))
        self.play(FadeOut(concl))


    def restrictions(self):
        title=TextMobject("Additional Considerations").scale(1.5)
        title2=TextMobject("Additional Considerations").to_corner(UL)
        self.play(Write(title))
        self.wait()
        self.play(Transform(title,title2))
        self.wait()
        one=TextMobject("walls").move_to(UP)
        two=TextMobject("speed")
        three=TextMobject("perfect information").move_to(DOWN)
        self.play(Write(one))
        self.wait()
        self.play(Write(two))
        self.wait()
        self.play(Write(three))
        self.wait()
        self.play(FadeOut(one),FadeOut(two),FadeOut(three),FadeOut(title))
        self.wait()


    def clear(self):
        path=Rectangle(height=2,width=0)
        g=TextMobject("G").move_to(0.5*DOWN)
        b=TextMobject("B").move_to(0.5*UP)
        self.play(FadeInFrom(path,UP),FadeInFrom(g,UP),FadeInFrom(b,UP))
        self.wait()
        self.play(FadeOut(path),FadeOut(g),FadeOut(b))
        self.wait()
    
    def variable(self):
        text=TextMobject("variable assignment")
        rect=Rectangle(height=2,width=2)
        into=Rectangle(height=0.5,width=0).move_to(1.25*DOWN)
        outof=Rectangle(height=0.5,width=0).move_to(1.25*UP)
        text.move_to(2*DOWN)
        label=TextMobject(r"$x$").move_to(1.5*LEFT)
        label2=TextMobject(r"$\neg x$").move_to(1.5*RIGHT)
        self.play(FadeIn(text))
        self.play(FadeInFrom(rect, UP),FadeInFrom(into, UP),FadeInFrom(outof,UP),FadeInFrom(label,UP),FadeInFrom(label2,UP))
        self.wait()
        g1=TextMobject("G").move_to(LEFT)
        g2=TextMobject("G").move_to(RIGHT)
        self.play(FadeIn(g1),FadeIn(g2))
        self.wait()
        self.play(FadeOut(g1),FadeOut(g2),FadeOut(text),FadeOut(rect),FadeOut(into),FadeOut(outof),FadeOut(label),FadeOut(label2))
        self.wait()
        circle=Circle()
        c=TextMobject(r"$x_i$")
        circle.surround(c)
        self.play(Write(c),Write(circle))
        self.wait()
        self.play(FadeOut(circle),FadeOut(c))
        self.wait()

    def clause(self):
        #text=TextMobject("clause")
        desc1=TextMobject("existential variables start with bananas on the paths")
        desc2=TextMobject("universal variables start with nothing on the paths")
        ex=TextMobject(r"$\forall x \exists y ((x\vee y)\wedge (\neg x \vee \neg y))$").move_to(3*UP)
        self.play(FadeIn(desc1.move_to(UP)))
        self.wait()
        self.play(FadeIn(desc2.move_to(DOWN)))
        self.wait()
        self.play(FadeOut(desc1),FadeOut(desc2))
        self.wait()
        self.play(FadeInFrom(ex, UP))
        clause1=TextMobject(r"$x \vee y$")
        rect1=Rectangle(height=2,width=2).move_to(3*LEFT)
        into1=Rectangle(height=0.5,width=0).move_to(1.25*DOWN+3*LEFT)
        outof1=Rectangle(height=0.5,width=0).move_to(1.25*UP+3*LEFT)
        clause1.move_to(2*DOWN+3*LEFT)
        label1_1=TextMobject(r"$x$").move_to(4.5*LEFT)
        label1_2=TextMobject(r"$y$").move_to(1.5*LEFT)
        banana1=TextMobject("B").move_to(2*LEFT)
        self.play(FadeInFrom(banana1,UP),FadeIn(clause1),FadeInFrom(rect1, UP),FadeInFrom(into1, UP),FadeInFrom(outof1,UP),FadeInFrom(label1_1,UP),FadeInFrom(label1_2,UP))
        self.wait()
        clause2=TextMobject(r"$\neg x \vee \neg y$")
        rect2=Rectangle(height=2,width=2).move_to(3*RIGHT)
        into2=Rectangle(height=0.5,width=0).move_to(1.25*DOWN+3*RIGHT)
        outof2=Rectangle(height=0.5,width=0).move_to(1.25*UP+3*RIGHT)
        clause2.move_to(2*DOWN+3*RIGHT)
        label2_1=TextMobject(r"$\neg y$").move_to(4.5*RIGHT)
        banana2=TextMobject("B").move_to(4*RIGHT)
        label2_2=TextMobject(r"$x$").move_to(1.5*RIGHT)
        self.play(FadeInFrom(banana2,UP),FadeIn(clause2),FadeInFrom(rect2, UP),FadeInFrom(into2, UP),FadeInFrom(outof2,UP),FadeInFrom(label2_1,UP),FadeInFrom(label2_2,UP))
        self.wait(3)
        self.play(FadeOut(ex),FadeOut(clause1),FadeOut(banana1),FadeOut(rect1),FadeOut(into1),FadeOut(outof1),FadeOut(label1_1),FadeOut(label1_2),FadeOut(clause2),FadeOut(banana2),FadeOut(rect2),FadeOut(into2),FadeOut(outof2),FadeOut(label2_1),FadeOut(label2_2))
        self.wait()
        circle=Circle()
        c=TextMobject(r"$c_i$")
        circle.surround(c)
        self.play(Write(c),Write(circle))
        self.wait()
        self.play(FadeOut(circle),FadeOut(c))
        self.wait()

class QSAT(Scene):
    def construct(self):
        text=TextMobject(r"What is $QSAT$?").scale(2)
        text2=TextMobject(r"$QSAT$: Given a QBF, is it satisfiable?").to_corner(UL)
        self.play(Write(text))
        self.wait()
        self.play(Transform(text,text2))
        self.wait()
        ex=TextMobject(r"$\varphi = \forall x \exists y ((x\vee y)\wedge (\neg x \vee \neg y))$").scale(0.85)
        self.play(FadeIn(ex.move_to(2*UP)))
        self.wait()
        exm=TextMobject(r"$\varphi = \forall x \exists y ((x\vee y)\wedge (\neg x \vee \neg y))$").scale(0.85).to_edge(UP)
        self.play(Transform(ex,exm),FadeOut(text))
        self.wait()
        exp1=TextMobject(r"\textbf{QSAT as a game:}").move_to(2*UP+4*LEFT)
        self.play(FadeIn(exp1))
        self.wait()
        exp2=TextMobject("2 players: U, E").move_to(UP)
        exp3=TextMobject(r"U $\to \,\forall$").move_to(0.5*UP)
        exp4=TextMobject(r"E $\to \, \exists$")
        self.play(FadeIn(exp2),FadeIn(exp3),FadeIn(exp4))
        self.wait()
        exp5=TextMobject(r"$QSAT(\varphi)$ outputs 1 iff $E$ can force a win.").move_to(DOWN)
        self.play(FadeIn(exp5))
        self.wait(6)

class Intro(Scene):
    def construct(self):
        title=TextMobject("How hard is Mario Kart Tour?").scale(2)
        self.play(Write(title))
        self.wait()
        self.play(LaggedStart(FadeOutAndShift, title))
        ans=TextMobject("Answer: PSPACE-hard").scale(1.5)
        self.play(Write(ans))
        self.wait()
        self.play(FadeOut(ans))
        self.wait()
        self.definition()
        strat=TextMobject(r"Proof strategy: Show $QSAT\leq_p MARIOKART$").to_edge(UP)
        self.play(Write(strat))
        self.wait()
        exp1=TextMobject(r"We will show how to convert any instance of $QSAT$").move_to(UP).scale(0.75)
        exp2=TextMobject(r"into an instance of $MARIOKART$.").move_to(0.5*UP).scale(0.75)
        self.play(FadeIn(exp1),FadeIn(exp2))
        self.wait()
        exp3=TextMobject(r"Since $QSAT$ is $PSPACE$-hard, it will follow that $MARIOKART$ is $PSPACE$-hard.").scale(0.75).move_to(1.5*DOWN)
        self.play(FadeIn(exp3))
        self.wait()

    def definition(self):
        exp1=TextMobject("Mario Kart Tour is a multiplayer racing game.").move_to(2.5*UP).scale(0.75)
        exp2=TextMobject("There are different modes, but we will focus on the racing mode.").move_to(2*UP).scale(0.75)
        exp3=TextMobject(r"A race takes place between $m$ different players on a track $T$.").move_to(1.5*UP).scale(0.75)
        exp4=TextMobject("A track can have varying length and items that players can pick up and use.").move_to(0.5*UP).scale(0.75)
        exp5=TextMobject("The relevant items we will consider are bananas (B) and green shells (G).").move_to(0*UP).scale(0.75)
        exp6=TextMobject("A player who hits a banana is temporarily slowed down.").move_to(DOWN).scale(0.75)
        exp7=TextMobject("A green shell can be used by a player to hit a banana out of the way.").move_to(1.5*DOWN).scale(0.75)
        exp8=TextMobject("There are many other items and track properties, but we will not need them.").move_to(2.5*DOWN).scale(0.75)
        exp9=TextMobject("The player who reaches the finish line first wins.").move_to(3*DOWN).scale(0.75)
        exp10=TextMobject(r"Define the $MARIOKART$ problem as follows:").scale(1.25)
        defn=TextMobject(r"Given a track $T$, can player $p$ force a win?").scale(1.25)
        self.play(FadeIn(exp1))
        self.wait()
        self.play(FadeIn(exp2))
        self.wait()
        self.play(FadeIn(exp3))
        self.wait()
        self.play(FadeIn(exp4))
        self.wait()
        self.play(FadeIn(exp5))
        self.wait()
        self.play(FadeIn(exp6))
        self.wait()
        self.play(FadeIn(exp7))
        self.wait()
        self.play(FadeIn(exp8))
        self.wait()
        self.play(FadeIn(exp9))
        self.wait()
        self.play(FadeOut(exp1),FadeOut(exp2),FadeOut(exp3),FadeOut(exp4),FadeOut(exp5),FadeOut(exp6),FadeOut(exp7),FadeOut(exp8),FadeOut(exp9))
        self.wait()
        self.play(Write(exp10))
        self.wait(2)
        self.play(FadeOut(exp10))
        self.wait()
        self.play(Write(defn))
        self.wait()
        self.play(FadeOut(defn))
        self.wait()