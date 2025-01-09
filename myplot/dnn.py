import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    
    # elements
    to_Element( "input1", s_filer=1, c_fier=1, n_filer=1, offset="(0,0,4)", to="(0,0,0)", width=2, height=2, depth=2, caption="Threshold" ),
    to_Element( "input2", s_filer=1, c_fier=1, n_filer=1, offset="(0,0,0)", to="(0,0,0)", width=2, height=2, depth=2, caption="Duration" ),
    to_Element( "input3", s_filer=1, c_fier=1, n_filer=1, offset="(0,0,-4)", to="(0,0,0)", width=2, height=2, depth=2, caption="Noise Level" ),
    to_Element( "input1-1", s_filer=1, c_fier=1, n_filer=1, offset="(3,0,0.45)", to="(input2-west)", width=2, height=2, depth=2, caption=" " ),
    to_Element( "input2-2", s_filer=1, c_fier=1, n_filer=1, offset="(3,0,0)", to="(input2-west)", width=2, height=2, depth=2, caption=" " ),
    to_Element( "input3-3", s_filer=1, c_fier=1, n_filer=1, offset="(3,0,-0.45)", to="(input2-west)", width=2, height=2, depth=2, caption=" " ),
    to_Signal( "input", s_filer=3, c_fier=1, n_filer=1, offset="(3,0,0)", to="(input2-west)", width=2, height=2, depth=6, caption="Input" ),
    to_FC("fc1", s_filer=16, c_fier=1, n_filer=1, offset="(2,0,0)", to="(input-east)", width=2, height=2, depth=32, caption="Dense1" ),
    to_RELU("rl1", s_filer=16, c_fier=1, n_filer=1, offset="(1,0,0)", to="(fc1-east)", width=2, height=2, depth=32, caption="ReLU" ),
    to_FC("fc2", s_filer=8, c_fier=1, n_filer=1, offset="(2,0,0)", to="(rl1-east)", width=2, height=2, depth=16, caption="Dense2" ),
    to_RELU("rl2", s_filer=8, c_fier=1, n_filer=1, offset="(1,0,0)", to="(fc2-east)", width=2, height=2, depth=16, caption="ReLU" ),
    to_FC("fc3", s_filer=4, c_fier=1, n_filer=1, offset="(2,0,0)", to="(rl2-east)", width=2, height=2, depth=8, caption="Dense3" ),
    to_RELU("rl3", s_filer=4, c_fier=1, n_filer=1, offset="(1,0,0)", to="(fc3-east)", width=2, height=2, depth=8, caption="ReLU" ),
    to_FC("output", s_filer=1, c_fier=1, n_filer=1, offset="(2,0,0)", to="(rl3-east)", width=2, height=2, depth=2, caption="Recall" ),
    
    # connections
    to_connect_east_near("input1", "input", 2.8, 0, 0),
    to_connection("input2", "input"),
    to_connect_east_far("input3", "input", 2.8, 0, 0),
    to_connection("input", "fc1"),
    to_connection("fc1", "rl1"),
    to_connection("rl1", "fc2"),
    to_connection("fc2", "rl2"),
    to_connection("rl2", "fc3"),
    to_connection("fc3", "rl3"),
    to_connection("rl3", "output"),
    to_dash_from_east("fc1", "rl1"),
    to_dash_from_east("fc2", "rl2"),
    to_dash_from_east("fc3", "rl3"),

    
    
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
