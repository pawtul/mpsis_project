/*********************************************
 * OPL 12.6.3.0 Model
 * Author: user
 * Creation Date: 06-12-2016 at 16:45:11
 *********************************************/
int n=  ...;//X calkowita ilosc nodow
int d= ...;//X ilosc nodow do wyrzucenia
range Nodes= 1 ..n;
int mat[Nodes][Nodes] = ...;//X macierz sasiedztw
dvar boolean x[Nodes][Nodes];//X macierz zbiorow podgrafow, kazdy wiersz to graf

minimize
	sum(a in Nodes) ((sum(b in Nodes) (x[a][b]))*((sum(b in Nodes) (x[a][b]))-1)/2);
 	
 subject to {
 	TotalAmmountOfNodes: 
 	(sum(a in Nodes) sum(b in Nodes) x[a][b])==n-d;//X zapewnia ilosc nodow rowna n-d
 	AmmountOfNodesPerColumn:
 	forall(a in Nodes) (sum(b in Nodes) x[b][a])<=1;//X zapewnia ze kazda kolumna ma nie wiecej niz 1 node(zaden nie zostanie wykorzystany 2 razy)
 	NoAdjacentNodesInDifferentRows: 		
	forall(a in Nodes, b in Nodes,c in Nodes,d in Nodes: mat[b][d]==1 && a!=c)  x[a][b]+x[c][d]<=1;//X nody w kolejnych wierszach sa rozlaczne
	
	//mnozenie razy ktorykolwiek z tego samego wiersza musi dawac 1 // nie jt wazne czy to jedne czy 2 podgrafy, im wiecej tym lepiej
	};

execute {
	writeln("mat=   ",mat);
	writeln("x=     ",x);	
}