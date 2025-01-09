import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    
    # elements
    to_Signal( "signal", s_filer=6000, c_fier=1, n_filer=1, offset="(0,0,0)", to="(0,0,0)", width=2, height=2, depth=40, caption="Signal" ),
    to_Signal( "time", s_filer=64, c_fier=1, n_filer=1, offset="(2,0,5)", to="(signal-east)", width=2, height=2, depth=15, caption="Time" ),
    to_Signal( "freq", s_filer=64, c_fier=1, n_filer=1, offset="(2,0,-5)", to="(signal-east)", width=2, height=2, depth=15, caption="Freq" ),
    to_Signal( "features", s_filer=128, c_fier=1, n_filer=1, offset="(5,0,0)", to="(signal-east)", width=2, height=2, depth=30, caption="Features" ),
    to_Filter( "filter1", s_filer=3, c_fier=1, n_filer=1, offset="(0,1,-2)", to="(features-west)", width=2, height=2, depth=6, caption=" " ),
    to_Filter( "filter2", s_filer=3, c_fier=1, n_filer=1, offset="(0,0,-2)", to="(features-west)", width=2, height=2, depth=6, caption=" " ),
    to_Filter( "filter3", s_filer=3, c_fier=1, n_filer=1, offset="(0,-1,-2)", to="(features-west)", width=2, height=2, depth=6, caption=" " ),
    to_Filters( "filter4", s_filer=3, c_fier=1, n_filer=1, offset="(0,-2,-2)", to="(features-west)", width=2, height=2, depth=6, caption="Filters" ),
    to_Conv("conv1", s_filer=128, c_fier=4, n_filer=1, offset="(3,0,0)", to="(features-east)", width=2, height=8, depth=30, caption="Conv" ),
    to_Element( "element", s_filer=1, c_fier=1, n_filer=1, offset="(0,0,-2)", to="(conv1-west)", width=2, height=2, depth=2, caption=" " ),
    to_BN("bn1", s_filer=128, c_fier=4, n_filer=1, offset="(2,0,0)", to="(conv1-east)", width=2, height=8, depth=30, caption="BN" ),
    to_RELU("rl1", s_filer=128, c_fier=4, n_filer=1, offset="(2,0,0)", to="(bn1-east)", width=2, height=8, depth=30, caption="ReLU" ),
    to_AVG("avg1", s_filer=1, c_fier=4, n_filer=1, offset="(2,0,0)", to="(rl1-east)", width=2, height=8, depth=2, caption="AvgPool" ),
    to_FC("fc1", s_filer=1, c_fier=4, n_filer=1, offset="(2,0,0)", to="(avg1-east)", width=2, height=8, depth=2, caption="FC" ),
    to_Element( "avgvec", s_filer=128, c_fier=1, n_filer=1, offset="(0,-0.25,0)", to="(rl1-west)", width=2, height=2, depth=30, caption=" " ),
    to_Element( "avgele", s_filer=1, c_fier=1, n_filer=1, offset="(0,-0.25,0)", to="(avg1-west)", width=2, height=2, depth=2, caption=" " ),
    to_SOFTMAX("softmax", s_filer=1, c_fier=4, n_filer=1, offset="(2,0,0)", to="(fc1-east)", width=2, height=8, depth=2, caption="Softmax" ),
    to_FC("output", s_filer=1, c_fier=1, n_filer=1, offset="(2,0,0)", to="(softmax-east)", width=2, height=2, depth=2, caption="Event Label" ),
    
    # connections
    to_connect_near_west("signal", "time", 0, 0, 1),
    to_connect_far_west("signal", "freq", 0, 0, -1),
    to_connect_east_near("time", "features", 2.8, 0, 0),
    to_connect_east_far("freq", "features", 2.8, 0, 0),
    to_connection("features", "conv1"),
    to_dash_from_west("element", "filter2"),
    to_connection("conv1", "bn1"),
    to_connection("bn1", "rl1"),
    to_connection("rl1", "avg1"),
    to_connection("avg1", "fc1"),
    to_dash_from_east("conv1", "bn1"),
    to_dash_from_east("bn1", "rl1"),
    to_dash_from_east("avgvec", "avgele"),
    to_connection("fc1", "softmax"),
    to_dash_from_east("fc1", "softmax"),
    to_connection("softmax", "output"),
    to_dash_from_east("softmax", "output"),
    
    
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
