import networkx as nx

def get_FG(name):
    if name =='COOH':
        G = nx.Graph()
        G.add_node(1,atom = 'C')
        G.add_node(2,atom = 'O')
        G.add_node(3,atom = 'O')
        G.add_node(4,atom = 'H')
        G.add_edge(1,3,bond_type='S')
        G.add_edge(1,2,bond_type='D')
        G.add_edge(3,4,bond_type='S')
    elif name =='F':
        G = nx.Graph()
        G.add_node(1,atom = 'F')
    elif name =='OMe':
        G = nx.Graph()
        G.add_node(1,atom = 'O')
        G.add_node(2,atom = 'C')
        G.add_node(3,atom = 'H')
        G.add_node(4,atom = 'H')
        G.add_node(5,atom = 'H')
        #c
        G.add_edge(2,1,bond_type='S')
        G.add_edge(2,4,bond_type='S')
        G.add_edge(2,5,bond_type='S')
        G.add_edge(2,3,bond_type='S')
    elif name =='H':
        ## count only H-C (suggest: team)
        G = nx.Graph()
        G.add_node(1,atom = 'H')
        G.add_node(2,atom = 'C')
        G.add_edge(1,2,bond_type='S')
    elif name =='NHMe':
        G = nx.Graph()
        G.add_node(1, atom = 'N')
        G.add_node(2, atom = 'C' )
        G.add_node(3, atom = 'H' )
        G.add_node(4, atom = 'H' )
        G.add_node(5, atom = 'H' )
        G.add_node(6, atom = 'H' )
        #n
        G.add_edge(1,2,bond_type='S')
        G.add_edge(1,3,bond_type='S')
        #c
        G.add_edge(2,4,bond_type='S')
        G.add_edge(2,5,bond_type='S')
        G.add_edge(2,6,bond_type='S')

    elif name =='Pr':
        G = nx.Graph()
        G.add_node(1,atom = 'C')
        G.add_node(2,atom = 'C')
        G.add_node(3,atom = 'C')
        G.add_node(4,atom = 'H')
        G.add_node(5,atom = 'H')
        G.add_node(6,atom = 'H')
        G.add_node(7,atom = 'H')
        G.add_node(8,atom = 'H')
        G.add_node(9,atom = 'H')
        G.add_node(10,atom = 'H')
        #c1
        G.add_edge(1,4,bond_type='S')
        G.add_edge(1,10,bond_type='S')
        G.add_edge(1,2,bond_type='S')
        #c2
        G.add_edge(2,9,bond_type='S')
        G.add_edge(2,5,bond_type='S')
        G.add_edge(2,3,bond_type='S')
        #c3
        G.add_edge(3,6,bond_type='S')
        G.add_edge(3,7,bond_type='S')
        G.add_edge(3,8,bond_type='S')
    elif name =='NH2':
        G = nx.Graph()
        G.add_node(1, atom = 'N')
        G.add_node(2, atom = 'H' )
        G.add_node(3, atom = 'H' )

        G.add_edge(1,2,bond_type='S')
        G.add_edge(1,3,bond_type='S')
    elif name =='Br':
        G = nx.Graph()
        G.add_node(1,atom = 'Br')
    elif name =='HCO':
        G = nx.Graph()
        G.add_node(1,atom = 'C')
        G.add_node(2,atom = 'O')
        G.add_node(3,atom = 'H')
        G.add_edge(1,2,bond_type='D')
        G.add_edge(1,3,bond_type='S')
    elif name =='SO3H':
        G = nx.Graph()
        G.add_node(1, atom = 'S')
        G.add_node(2, atom = 'O')
        G.add_node(3, atom = 'O')
        G.add_node(4, atom = 'O')
        G.add_node(5, atom = 'H')
        #S
        G.add_edge(1,2,bond_type='D')
        G.add_edge(1,3,bond_type='S')
        G.add_edge(1,4,bond_type='D')
        #O
        G.add_edge(3,5,bond_type='S')
    elif name =='Me':
        G = nx.Graph()
        G.add_node(1, atom = 'C')
        G.add_node(2, atom = 'H')
        G.add_node(3, atom = 'H')
        G.add_node(4, atom = 'H')

        G.add_edge(1,2,bond_type='S')
        G.add_edge(1,3,bond_type='S')
        G.add_edge(1,4,bond_type='S')
    elif name =='OEt':
        G = nx.Graph()
        G.add_node(1,atom = 'O')
        G.add_node(2,atom = 'C')
        G.add_node(3,atom = 'C')
        G.add_node(4,atom = 'H')
        G.add_node(5,atom = 'H')
        G.add_node(6,atom = 'H')
        G.add_node(7,atom = 'H')
        G.add_node(8,atom = 'H')

        #c1
        G.add_edge(2,1,bond_type='S')
        G.add_edge(2,4,bond_type='S')
        G.add_edge(2,8,bond_type='S')
        G.add_edge(2,3,bond_type='S')
        #c2
        G.add_edge(3,5,bond_type='S')
        G.add_edge(3,6,bond_type='S')
        G.add_edge(3,7,bond_type='S')
    elif name =='Cl':
        G = nx.Graph()
        G.add_node(1,atom = 'Cl')
    elif name =='CN':
        G = nx.Graph()
        G.add_node(1, atom = 'C')
        G.add_node(2, atom = 'N' )
        G.add_edge(1,2,bond_type='T')
    elif name =='Et':
        G = nx.Graph()
        G.add_node(1,atom = 'C')
        G.add_node(2,atom = 'C')
        G.add_node(3,atom = 'H')
        G.add_node(4,atom = 'H')
        G.add_node(5,atom = 'H')
        G.add_node(6,atom = 'H')
        G.add_node(7,atom = 'H')
        #c1
        G.add_edge(1,3,bond_type='S')
        G.add_edge(1,7,bond_type='S')
        G.add_edge(1,6,bond_type='S')
        #c2
        G.add_edge(2,4,bond_type='S')
        G.add_edge(2,5,bond_type='S')
        #c-c
        G.add_edge(2,1,bond_type='S')
    elif name =='OH':
        G = nx.Graph()
        G.add_node(1,atom = 'O')
        G.add_node(2,atom = 'H')
        G.add_edge(1,2,bond_type='S')
    elif name =='NO2':
        G = nx.Graph()
        G.add_node(1, atom = 'N')
        G.add_node(2, atom = 'O' )
        G.add_node(3, atom = 'O' )

        G.add_edge(1,2,bond_type='A')
        G.add_edge(1,3,bond_type='A')

    elif name =='OPr':
        G = nx.Graph()
        G.add_node(1,atom = 'C')
        G.add_node(2,atom = 'C')
        G.add_node(3,atom = 'C')
        G.add_node(4,atom = 'H')
        G.add_node(5,atom = 'H')
        G.add_node(6,atom = 'H')
        G.add_node(7,atom = 'H')
        G.add_node(8,atom = 'H')
        G.add_node(9,atom = 'H')
        G.add_node(10,atom = 'H')
        G.add_node(11,atom = 'O')

        #c1
        G.add_edge(1,4,bond_type='S')
        G.add_edge(1,10,bond_type='S')
        G.add_edge(1,2,bond_type='S')
        G.add_edge(1,11,bond_type='S')

        #c2
        G.add_edge(2,9,bond_type='S')
        G.add_edge(2,5,bond_type='S')
        G.add_edge(2,3,bond_type='S')
        #c3
        G.add_edge(3,6,bond_type='S')
        G.add_edge(3,7,bond_type='S')
        G.add_edge(3,8,bond_type='S')
    elif name =='Ph':
        G = nx.Graph()
        G.add_node(1, atom = 'C')
        G.add_node(2, atom = 'C')
        G.add_node(3, atom = 'C')
        G.add_node(4, atom = 'C')
        G.add_node(5, atom = 'C')
        G.add_node(6, atom = 'C')
        G.add_node(7, atom = 'H')
        G.add_node(8, atom = 'H')
        G.add_node(9, atom = 'H')
        G.add_node(10, atom = 'H')
        G.add_node(11, atom = 'H')
        #C
        G.add_edge(1,2,bond_type='A')
        G.add_edge(2,3,bond_type='A')
        G.add_edge(3,4,bond_type='A')
        G.add_edge(4,5,bond_type='A')
        G.add_edge(5,6,bond_type='A')
        G.add_edge(6,1,bond_type='A')
        #H
        G.add_edge(2,7,bond_type='S')
        G.add_edge(3,8,bond_type='S')
        G.add_edge(4,9,bond_type='S')
        G.add_edge(5,10,bond_type='S')
        G.add_edge(6,11,bond_type='S')
    elif name =='I':
        G = nx.Graph()
        G.add_node(1,atom = 'I')
    return G
        
        
        
        
        
        
        
        
        
        