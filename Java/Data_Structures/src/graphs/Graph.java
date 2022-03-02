package graphs;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Set;
import java.util.TreeMap;

/**
 * Implements a graph. We use two maps: one map for adjacency properties 
 * (adjancencyMap) and one map (dataMap) to keep track of the data associated 
 * with a vertex. 
 */
public class Graph<E> {

	private static class Vertex implements Comparable<Vertex> { 
		private String vertexName; 
		private Vertex predecessor; 
		private int costFromStart = Integer.MAX_VALUE; 

		private Vertex(String vertexName) {  	
			this.vertexName = vertexName; 
			this.predecessor = null; 
		}

		public String toString() { 
			return "{Name:" + this.vertexName + ", Cost:" + costFromStart+ "}"; 
		}

		@Override 
		public boolean equals(Object obj) { 
			if(!(obj instanceof Graph.Vertex)) { 
				return false; 
			} 

			if(this == obj) { 
				return true; 
			} 

			Vertex v = (Graph.Vertex) obj; 
			if(this.vertexName.equals(v.vertexName)){ 
				return true; 
			} 

			return false; 
		}  

		@Override
		public int compareTo(Vertex o) {
			return this.costFromStart - o.costFromStart;
		} 

	}

	private HashMap<String, HashMap<String, Integer>> adjacencyMap;
	private HashMap<String, E> dataMap;

	public void addVertex(String vertexName, E data) { 
		if(adjacencyMap == null) { 
			adjacencyMap = new HashMap<>(); 
			dataMap = new HashMap<>(); 

		}	
		/* Execute the data already exists in the Graph */ 
		if(dataMap.get(vertexName) != null) { 
			throw new IllegalArgumentException("Vertex exists in graph"); 

		}

		adjacencyMap.put(vertexName, null); 
		dataMap.put(vertexName, data); 
	}

	public void addDirectedEdge(String startVertexName, String endVertexName, 
			int cost) { 
		HashMap<String, Integer> entry = null; 
		if(adjacencyMap.get(startVertexName) == null) { 
			entry = new HashMap<>(); 

		} else { 
			entry = adjacencyMap.get(startVertexName); 

		}
		entry.put(endVertexName, cost); 
		adjacencyMap.put(startVertexName, entry); 
	}

	public int doDijkstras(String startVertexName, String  endVertexName, ArrayList<String> shortestPath) { 
		PriorityQueue<Vertex> minqueue = genQueue(); 
		ArrayList<Vertex> shortestPathV = new ArrayList<>(); 

		Vertex endVertex = null; 

		/* Set the 'start' vertex cost to 0 */ 
		Vertex start = new Vertex(startVertexName); 
		start.costFromStart = 0; 
		minqueue.offer(start); 

		while(!shortestPathV.contains(new Vertex(endVertexName))) { 
			Vertex currVertex = minqueue.poll(); 
			endVertex = currVertex; 

			shortestPathV.add(currVertex);

			HashMap<String, Integer> adjacents = adjacencyMap.get(currVertex.vertexName); 
			
			/* Execute if this vertex has no adjacent vertices */ 
			if(adjacents == null) { 
				continue;
			}
			
			for(String adj: adjacents.keySet()) { 
				if(currVertex.costFromStart + adjacents.get(adj) < costFromStart(adj, 
						new PriorityQueue<Vertex>(minqueue))) { 					
					Vertex j = new Vertex(adj);
					j.costFromStart = currVertex.costFromStart + adjacents.get(adj); 
					j.predecessor = currVertex; 

					minqueue.remove(new Vertex(adj)); 
					minqueue.add(j); 
				}
			}
		}
		
		/* Execute if there is no existing path to 'endVertex' */ 
		if(endVertex.costFromStart == Integer.MAX_VALUE) { 
			shortestPath.add("None"); 
			return -1; 
		}
		
		genShortestPath(shortestPathV, shortestPath, endVertexName); 
		return endVertex.costFromStart; 
	}

	public Map<String, Integer> getAdjacentVertices(String vertexName) { 
		return new TreeMap<String, Integer>(adjacencyMap.get(vertexName)); 
	}

	public int getCost(String startVertexName, String endVertexName) { 
		return adjacencyMap.get(startVertexName).get(endVertexName); 
	}

	public E getData(String vertex) { 
		return dataMap.get(vertex); 
	}

	public Set<String> getVertices() { 
		return dataMap.keySet(); 
	}

	public String toString() { 
		TreeMap<String, HashMap<String, Integer>> x = new TreeMap<>(adjacencyMap);

		String retVal = ""; 
		retVal += "Vertices: " + x.keySet() + "\n"; 
		retVal += "Edges: \n"; 
		while(x.size() > 0) { 
			retVal += "Vertex(" + x.firstKey() + ")--->";
			if(x.get(x.firstKey()) != null) {
				retVal += x.get(x.firstKey()); 

			}
			else {
				retVal += "{}"; 
			}
			retVal += "\n"; 
			x.remove(x.firstKey()); 

		}
		return retVal; 
	}

	private int costFromStart(String vertexName, PriorityQueue<Vertex> p) { 
		while(p.size() > 0) { 
			Vertex v = p.poll();
			if(v.vertexName.equals(vertexName)) { 
				return v.costFromStart; 
			}
		}

		return -1; 
	}

	private PriorityQueue<Vertex> genQueue() { 
		PriorityQueue<Vertex> retQueue = new PriorityQueue<>(); 
		for(String s: adjacencyMap.keySet()) { 
			retQueue.offer(new Vertex(s)); 
		}
		return retQueue; 
	}

	private static void genShortestPath(ArrayList<Vertex> shortestPathV, ArrayList<String> shortestPath,
			String endVertexName
			) { 
		/* Store the array that will be our shortestPath */
		for(int i = 0; i < shortestPathV.size(); i++) { 
			shortestPath.add(shortestPathV.get(i).vertexName); 
		}

		/* Store the list of predecessors for vertices in shortestPath: 
		 * We check the shortestPath's vertices against the list of predecessors */ 
		ArrayList<String> predecessors = new ArrayList<>(); 
		for(int i = 0; i < shortestPathV.size(); i++) { 
			/* Omit the predecessor of the 'start' vertex  */ 
			if(!(shortestPathV.get(i).predecessor == null)) { 				
				predecessors.add(shortestPathV.get(i).predecessor.vertexName); 
			}
		}

		int size = shortestPath.size(); 
		for(int i = 0; i < size; i++) { 
			if(i >= shortestPath.size()) { 
				break; 
			}
			String s = shortestPath.get(i); 
			if(!predecessors.contains(s) && !s.equals(endVertexName)) { 
				shortestPath.remove(s); 
			}
		}
	}
}