from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        ## Hosts
        
        host11 = self.addHost( 'h11', mac='00:00:00:00:01:01', ip='10.0.0.1/8' )
        host12 = self.addHost( 'h12', mac='00:00:00:00:00:02', ip='10.0.0.2/8' )
        host13 = self.addHost( 'h13', mac='00:00:00:00:00:03', ip='10.0.0.3/8' )
        host14 = self.addHost( 'h14', mac='00:00:00:00:00:04', ip='10.0.0.4/8' )
        
        host21 = self.addHost( 'h21', mac='00:00:00:00:00:05', ip='10.0.0.5/8' )
        host22 = self.addHost( 'h22', mac='00:00:00:00:00:06', ip='10.0.0.6/8' )
        host23 = self.addHost( 'h23', mac='00:00:00:00:00:07', ip='10.0.0.7/8' )
        host24 = self.addHost( 'h24', mac='00:00:00:00:00:08', ip='10.0.0.8/8' )
        
        host31 = self.addHost( 'h31', mac='00:00:00:00:00:09', ip='10.0.0.9/8' )
        host32 = self.addHost( 'h32', mac='00:00:00:00:00:10', ip='10.0.0.10/8' )
        host33 = self.addHost( 'h33', mac='00:00:00:00:00:11', ip='10.0.0.11/8' )
        host34 = self.addHost( 'h34', mac='00:00:00:00:00:12', ip='10.0.0.12/8' )
    
        host41 = self.addHost( 'h41', mac='00:00:00:00:00:13', ip='10.0.0.13/8' )
        host42 = self.addHost( 'h42', mac='00:00:00:00:00:14', ip='10.0.0.14/8' )
        host43 = self.addHost( 'h43', mac='00:00:00:00:00:15', ip='10.0.0.15/8' )
        host44 = self.addHost( 'h44', mac='00:00:00:00:00:16', ip='10.0.0.16/8' )
        
        ## Switches

        switch01 = self.addSwitch( 's01', mac='00:00:00:00:01:01' )
        switch02 = self.addSwitch( 's02', mac='00:00:00:00:01:02' )
        switch03 = self.addSwitch( 's03', mac='00:00:00:00:01:03' )
        switch04 = self.addSwitch( 's04', mac='00:00:00:00:01:04' )

        switch11 = self.addSwitch( 's11', mac='00:00:00:00:01:05' )
        switch12 = self.addSwitch( 's12', mac='00:00:00:00:01:06' )
        switch13 = self.addSwitch( 's13', mac='00:00:00:00:01:07' )
        switch14 = self.addSwitch( 's14', mac='00:00:00:00:01:08' )
        switch15 = self.addSwitch( 's15', mac='00:00:00:00:01:09' )
        switch16 = self.addSwitch( 's16', mac='00:00:00:00:01:10' )
        switch17 = self.addSwitch( 's17', mac='00:00:00:00:01:11' )
        switch18 = self.addSwitch( 's18', mac='00:00:00:00:01:12' )

        switch21 = self.addSwitch( 's21', mac='00:00:00:00:01:13' )
        switch22 = self.addSwitch( 's22', mac='00:00:00:00:01:14' )
        switch23 = self.addSwitch( 's23', mac='00:00:00:00:01:15' )
        switch24 = self.addSwitch( 's24', mac='00:00:00:00:01:16' )
        switch25 = self.addSwitch( 's25', mac='00:00:00:00:01:17' )
        switch26 = self.addSwitch( 's26', mac='00:00:00:00:01:18' )
        switch27 = self.addSwitch( 's27', mac='00:00:00:00:01:19' )
        switch28 = self.addSwitch( 's28', mac='00:00:00:00:01:20' )

        # Add links
        self.addLink( switch01, switch11 )
        self.addLink( switch01, switch13 )
        self.addLink( switch01, switch15 )
        self.addLink( switch01, switch17 )
        
        self.addLink( switch02, switch11 )
        self.addLink( switch02, switch13 )
        self.addLink( switch02, switch15 )
        self.addLink( switch02, switch17 )
        
        self.addLink( switch03, switch12 )
        self.addLink( switch03, switch14 )
        self.addLink( switch03, switch16 )
        self.addLink( switch03, switch18 )
        
        self.addLink( switch04, switch12 )
        self.addLink( switch04, switch14 )
        self.addLink( switch04, switch16 )
        self.addLink( switch04, switch18 )

        ##################################

        self.addLink( switch11, switch21 )
        self.addLink( switch11, switch22 )
        self.addLink( switch12, switch21 )
        self.addLink( switch12, switch22 )

        self.addLink( switch13, switch23 )
        self.addLink( switch13, switch24 )
        self.addLink( switch14, switch23 )
        self.addLink( switch14, switch24 )

        self.addLink( switch15, switch25 )
        self.addLink( switch15, switch26 )
        self.addLink( switch16, switch25 )
        self.addLink( switch16, switch26 )

        self.addLink( switch17, switch27 )
        self.addLink( switch17, switch28 )
        self.addLink( switch18, switch27 )
        self.addLink( switch18, switch28 )

        ##################################

        self.addLink( host11, switch21 )
        self.addLink( host12, switch21 )
        self.addLink( host13, switch22 )
        self.addLink( host14, switch22 )

        self.addLink( host21, switch23 )
        self.addLink( host22, switch23 )
        self.addLink( host23, switch24 )
        self.addLink( host24, switch24 )

        self.addLink( host31, switch25 )
        self.addLink( host32, switch25 )
        self.addLink( host33, switch26 )
        self.addLink( host34, switch26 )

        self.addLink( host41, switch27 )
        self.addLink( host42, switch27 )
        self.addLink( host43, switch28 )
        self.addLink( host44, switch28 )

topos = { 'mytopo': ( lambda: MyTopo() ) }
