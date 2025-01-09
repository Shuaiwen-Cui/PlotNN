
import os

def to_head( projectpath ):
    pathlayers = os.path.join( projectpath, 'layers/' ).replace('\\', '/')
    return r"""
\documentclass[border=8pt, multi, tikz]{standalone} 
\usepackage{import}
\subimport{"""+ pathlayers + r"""}{init}
\usetikzlibrary{positioning}
\usetikzlibrary{3d} %for including external image 
"""

def to_cor():
    return r"""
\def\SignalColor{rgb:yellow,5;red,2.5;white,5}
\def\FilterColor{rgb:yellow,5;red,5;white,5}
\def\ConvColor{rgb:yellow,5;red,2.5;white,5}
\def\ConvReluColor{rgb:yellow,5;red,5;white,5}
\def\PoolColor{rgb:red,1;black,0.3}
\def\UnpoolColor{rgb:blue,2;green,1;black,0.3}
\def\FcColor{rgb:blue,5;red,2.5;white,5}
\def\FcReluColor{rgb:blue,5;red,5;white,4}
\def\SoftmaxColor{rgb:magenta,5;black,7}   
\def\SumColor{rgb:blue,5;green,15}
"""

def to_begin():
    return r"""
\newcommand{\copymidarrow}{\tikz \draw[-Stealth,line width=0.8mm,draw={rgb:blue,4;red,1;green,1;black,3}] (-0.3,0) -- ++(0.3,0);}

\begin{document}
\begin{tikzpicture}
\tikzstyle{connection}=[ultra thick,every node/.style={sloped,allow upside down},draw=\edgecolor,opacity=0.7]
\tikzstyle{copyconnection}=[ultra thick,every node/.style={sloped,allow upside down},draw={rgb:blue,4;red,1;green,1;black,3},opacity=0.7]
"""

# layers definition

def to_input( pathfile, to='(-3,0,0)', width=8, height=8, name="temp" ):
    return r"""
\node[canvas is zy plane at x=0] (""" + name + """) at """+ to +""" {\includegraphics[width="""+ str(width)+"cm"+""",height="""+ str(height)+"cm"+"""]{"""+ pathfile +"""}};
"""

# Signal
def to_Signal( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" " ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +r""",
        xlabel={{"""+ str(n_filer) +""", }},
        zlabel="""+ str(s_filer) +""",
        fill=\SignalColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

# Filter
def to_Filter( name, s_filer=3, n_filer=1, offset="(0,0,0)", to="(0,0,0)", width=2, height=2, depth=6, caption=" " ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +r""",
        xlabel={{"""+ str(n_filer) +""", }},
        zlabel="""+ str(s_filer) +""",
        fill=\FilterColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

# Conv
def to_Conv( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" " ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +r""",
        xlabel={{"""+ str(n_filer) +""", }},
        zlabel="""+ str(s_filer) +""",
        fill=\SignalColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

# Conv,Conv,relu
# Bottleneck
def to_ConvConvRelu( name, s_filer=256, n_filer=(64,64), offset="(0,0,0)", to="(0,0,0)", width=(2,2), height=40, depth=40, caption=" " ):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {RightBandedBox={
        name="""+ name +""",
        caption="""+ caption +""",
        xlabel={{ """+ str(n_filer[0]) +""", """+ str(n_filer[1]) +""" }},
        zlabel="""+ str(s_filer) +""",
        fill=\ConvColor,
        bandfill=\ConvReluColor,
        height="""+ str(height) +""",
        width={ """+ str(width[0]) +""" , """+ str(width[1]) +""" },
        depth="""+ str(depth) +"""
        }
    };
"""



# Pool
def to_Pool(name, offset="(0,0,0)", to="(0,0,0)", width=1, height=32, depth=32, opacity=0.5, caption=" "):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {Box={
        name="""+name+""",
        caption="""+ caption +r""",
        fill=\PoolColor,
        opacity="""+ str(opacity) +""",
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

# unpool4, 
def to_UnPool(name, offset="(0,0,0)", to="(0,0,0)", width=1, height=32, depth=32, opacity=0.5, caption=" "):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {Box={
        name="""+ name +r""",
        caption="""+ caption +r""",
        fill=\UnpoolColor,
        opacity="""+ str(opacity) +""",
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""



def to_ConvRes( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=6, height=40, depth=40, opacity=0.2, caption=" " ):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {RightBandedBox={
        name="""+ name + """,
        caption="""+ caption + """,
        xlabel={{ """+ str(n_filer) + """, }},
        zlabel="""+ str(s_filer) +r""",
        fill={rgb:white,1;black,3},
        bandfill={rgb:white,1;black,2},
        opacity="""+ str(opacity) +""",
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""


# ConvSoftMax
def to_ConvSoftMax( name, s_filer=40, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" " ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +""",
        zlabel="""+ str(s_filer) +""",
        fill=\SoftmaxColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

# SoftMax
def to_SoftMax( name, s_filer=10, offset="(0,0,0)", to="(0,0,0)", width=1.5, height=3, depth=25, opacity=0.8, caption=" " ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +""",
        xlabel={{" ","dummy"}},
        zlabel="""+ str(s_filer) +""",
        fill=\SoftmaxColor,
        opacity="""+ str(opacity) +""",
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

# Sum
def to_Sum( name, offset="(0,0,0)", to="(0,0,0)", radius=2.5, opacity=0.6):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Ball={
        name=""" + name +""",
        fill=\SumColor,
        opacity="""+ str(opacity) +""",
        radius="""+ str(radius) +""",
        logo=$+$
        }
    };
"""

# Multiply
def to_Mul( name, offset="(0,0,0)", to="(0,0,0)", radius=2.5, opacity=0.6):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Ball={
        name=""" + name +""",
        fill=\SumColor,
        opacity="""+ str(opacity) +""",
        radius="""+ str(radius) +""",
        logo=$\\times$
        }
    };
"""


def to_connection( of, to):
    return r"""
\draw [connection]  ("""+of+"""-east)    -- node {\midarrow} ("""+to+"""-west);
"""

def to_skip( of, to, pos=1.25):
    return r"""
\path ("""+ of +"""-southeast) -- ("""+ of +"""-northeast) coordinate[pos="""+ str(pos) +"""] ("""+ of +"""-top) ;
\path ("""+ to +"""-south)  -- ("""+ to +"""-north)  coordinate[pos="""+ str(pos) +"""] ("""+ to +"""-top) ;
\draw [copyconnection]  ("""+of+"""-northeast)  
-- node {\copymidarrow}("""+of+"""-top)
-- node {\copymidarrow}("""+to+"""-top)
-- node {\copymidarrow} ("""+to+"""-north);
"""

def to_connect_from_north( of, to):  # connection from north to west
    return r"""
\draw [connection]  ("""+of+"""-north)  -- node {\midarrow} ("""+to+"""-west -| """+of+"""-north) -- node {\midarrow} ("""+to+"""-west);
"""


def to_connect_from_south( of, to):  # connection from south to west
    return r"""
\draw [connection]  ("""+of+"""-south)  -- node {\midarrow} ("""+to+"""-west -| """+of+"""-south) -- node {\midarrow} ("""+to+"""-west);
"""


def to_connect_to_north( of, to):  # connection from east to north
    return r"""
\draw [connection]  ("""+of+"""-east)  -- node {\midarrow} ("""+of+"""-east -| """+to+"""-north) -- node {\midarrow} ("""+to+"""-north);
"""


def to_connect_to_south( of, to):   # connection from east to south
    return r"""
\draw [connection]  ("""+of+"""-east)  -- node {\midarrow} ("""+of+"""-east -| """+to+"""-south) -- node {\midarrow} ("""+to+"""-south);
"""

def to_connect_near_west( of, to, x, y, z):  # connection from near to west
    location = "("+str(x)+","+str(y)+","+str(z)+")"
    return r"""
\draw [connection]  ("""+of+"""-near)  -- node {\midarrow} ++"""+location+""" -- node {\midarrow} ("""+to+"""-west);
"""

def to_connect_far_west( of, to, x, y, z):  # connection from far to west
    location = "("+str(x)+","+str(y)+","+str(z)+")"
    return r"""
\draw [connection]  ("""+of+"""-far)  -- node {\midarrow} ++"""+location+""" -- node {\midarrow} ("""+to+"""-west);
"""
def to_connect_east_near( of, to, x, y, z):  # connection from east to near
    location = "("+str(x)+","+str(y)+","+str(z)+")"
    return r"""
\draw [connection]  ("""+of+"""-east)  -- node {\midarrow} ++"""+location+""" -- node {\midarrow} ("""+to+"""-near);
"""

def to_connect_east_far( of, to, x, y, z):  # connection from east to far
    location = "("+str(x)+","+str(y)+","+str(z)+")"
    return r"""
\draw [connection]  ("""+of+"""-east)  -- node {\midarrow} ++"""+location+""" -- node {\midarrow} ("""+to+"""-far);
"""


def to_dash_from_north( of, to):
    return r"""
\draw[densely dashed]
    ("""+of+"""-nearnorthwest) -- ("""+to+"""-nearsouthwest)
    ("""+of+"""-nearnortheast) -- ("""+to+"""-nearsoutheast)
    ("""+of+"""-farnortheast) -- ("""+to+"""-farsoutheast)
    ("""+of+"""-farnorthwest) -- ("""+to+"""-farsouthwest);
"""

def to_dash_from_south( of, to):
    return r"""
\draw[densely dashed]
    ("""+of+"""-nearsouthwest) -- ("""+to+"""-nearnorthwest)
    ("""+of+"""-nearsoutheast) -- ("""+to+"""-nearnortheast)
    ("""+of+"""-farsoutheast) -- ("""+to+"""-farnortheast)
    ("""+of+"""-farsouthwest) -- ("""+to+"""-farnorthwest);
"""


def to_dash_from_west( of, to):
    return r"""
\draw[densely dashed]
    ("""+of+"""-nearsouthwest) -- ("""+to+"""-nearsoutheast)
    ("""+of+"""-nearnorthwest) -- ("""+to+"""-nearnortheast)
    ("""+of+"""-farsouthwest) -- ("""+to+"""-farsoutheast)
    ("""+of+"""-farnorthwest) -- ("""+to+"""-farnortheast);
"""


def to_dash_from_east( of, to):
    return r"""
\draw[densely dashed]
    ("""+of+"""-nearsoutheast) -- ("""+to+"""-nearsouthwest)
    ("""+of+"""-nearnortheast) -- ("""+to+"""-nearnorthwest)
    ("""+of+"""-farsoutheast) -- ("""+to+"""-farsouthwest)
    ("""+of+"""-farnortheast) -- ("""+to+"""-farnorthwest);
"""

def to_end():
    return r"""
\end{tikzpicture}
\end{document}
"""


def to_generate( arch, pathname="file.tex" ):
    with open(pathname, "w") as f: 
        for c in arch:
            print(c)
            f.write( c )
     


