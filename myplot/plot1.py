import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    
    to_Signal( "signal", s_filer=6000, n_filer=1, offset="(0,0,0)", to="(0,0,0)", width=2, height=2, depth=40, caption="raw signal" ),
    to_Signal( "time", s_filer=64, n_filer=1, offset="(3,0,5)", to="(0,0,0)", width=2, height=2, depth=15, caption="time-domain" ),
    to_Signal( "freq", s_filer=64, n_filer=1, offset="(3,0,-5)", to="(0,0,0)", width=2, height=2, depth=15, caption="freq-domain" ),
    to_connect_near_west("signal", "time", 0, 0, 1),
    to_connect_far_west("signal", "freq", 0, 0, -1),
    to_Signal( "features", s_filer=128, n_filer=1, offset="(6,0,0)", to="(0,0,0)", width=2, height=2, depth=30, caption="features" ),
    to_connect_east_near("time", "features", 2.8, 0, 0),
    to_connect_east_far("freq", "features", 2.8, 0, 0),
    # to_Filter( "filter", s_filer=3, n_filer=1, offset="(0,0,3)", to="(0,0,0)", width=2, height=2, depth=6, caption="filter" ),
    # to_Conv("conv1", 512, 64, offset="(0,0,0)", to="(0,0,0)", height=64, depth=64, width=2 ),
    # to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)"),
    # to_Conv("conv2", 128, 64, offset="(1,0,0)", to="(pool1-east)", height=32, depth=32, width=2 ),
    # to_connection( "pool1", "conv2"),
    # to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=28, depth=28, width=1),
    # to_SoftMax("soft1", 10 ,"(3,0,0)", "(pool1-east)", caption="SOFT"  ),
    # to_Mul("name"),
    # to_connection("pool2", "soft1"),
    
    
    
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
