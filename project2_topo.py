#!/usr/bin/env python

"""
"""
from mininet.topo import Topo

class Tree( Topo ):
    "Internet Topology Zoo Specimen."

    def addSwitch( self, name, **opts ):
        kwargs = { 'protocols' : 'OpenFlow13' }
        kwargs.update( opts )
        return super(Tree, self).addSwitch( name, **kwargs )

    def __init__( self ):
        "Create a topology."

        # Initialize Topology
        Topo.__init__( self )
	
	s1 = self.addSwitch( 's1' )
	s2 = self.addSwitch( 's2' )
	s3 = self.addSwitch( 's3' )
	s4 = self.addSwitch( 's4' )
	
	h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')
        h10 = self.addHost('h10')


	
	self.addLink( s1, s2, bw=150 )
	self.addLink( s1, s3, bw=50 )
	self.addLink( s1, s4, bw=100 )
        #h1s2 = {'bw':234,'delay':'25'}
        self.addLink(h1, s2)

	#self.addLink( s2, h1 )
	self.addLink( s2, h2 )
	self.addLink( s2, h3 )
	self.addLink( s3, h4 )
	self.addLink( s3, h5 )
	self.addLink( s3, h6 )
	self.addLink( s4, h7 )
	self.addLink( s4, h8 )
	self.addLink( s4, h9 )
        self.addLink( s1, h10)


topos = { 'project2_topo': ( lambda: Tree() ) }

if __name__ == '__main__':
    from onosnet import run
    run( Tree() )

