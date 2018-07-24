class Task:
	"""Classe définissant une tâche de la TODO liste par:
		-L'intitulé de la tâche
		-L'ordre de priorité  """

	instances = []		  #liste de toutes les tâches deja creees"

	def __init__(self,description):
		"""Constructeur de la classe Task, la tache sera placée a la fin de la liste lors de sa creation"""
		self._description = description
		self._ordre = len(Task.instances) +1
		Task.instances.append(self)

	def _getDescription(self):
		"""accesseur de l'attribut Description"""	
		return(self._description)
    
	def _getOrdre(self):
		"""accesseur de l'attribut Ordre"""
		return(self._ordre)		

	def _setDescription(self,newDescription):
		"""Mutateur de l'attribut Description"""
		self._description = newDescription

	def _setOrdre(self,newOrdre):
		"""mutateur de l'attribut Ordre, qui ordonne les taches dynamiquement lorsqu'on en déplace une"""
		if self.ordre < newOrdre:    #Traitement lorsqu'on fait descendre une tache dans la liste
			for tache in Task.instances:
				if(tache._ordre <= newOrdre) & (tache._ordre > self.ordre):     #toutes les taches comprises entre celle que je souhaite deplacer (exclue) et sa nouvelle position (inclue)
					tache._ordre-=1
		else:						 #Traitement lorsqu'on fait monter une tache dans la liste
			for tache in Task.instances:
				if (tache._ordre >= newOrdre) & ( tache._ordre < self.ordre):   #toutes les taches comprises entre celle que je souhaite deplacer (exclue) et sa nouvelle position (inclue)
					tache._ordre+=1				
		self._ordre=newOrdre				#finalement, je deplace la tache voulue

	def supprimerTache(self):
		"""methode de suppression d'une tache, et reorganise celles situées en dessous dans la liste"""
		for tache in Task.instances:
			if(tache._ordre > self._ordre):
				tache._ordre -= 1
		Task.instances.remove(self)

	def afficherTODO(cls):
		"""methode d'affichage de la liste entiere"""
		Task.instances.sort(key = lambda task : task._ordre)
		for tache in Task.instances:
			print(tache)
		print()		

	def __str__(self):
		"""Méthode d'affichage d'un objet Task"""

		return "{}.{}".format(self.ordre,self.description)

	ordre = property( _getOrdre, _setOrdre)
	description = property( _getDescription, _setDescription)

""" Tests en dur de la classe Task :

           modif ordre         ajout tache +modif ordre      suppr. tache              	ajout tache
			  
	1.Lait	   		   1.Train               1.Train                   1.Train 				        1.Train
	2.Lessive   ---->  2.Lait     ---------> 2.BilletRetour  ------->  2.BilletRetour    ------->   2.BilletRetour
	3.Train	           3.Lessive             3.Lait                    3.lessive			        3.Lessive
	                                         4.lessive									            4.Faire les courses

"""

lait,lessive,train=Task("Acheter du lait"),Task("Faire une lessive"),Task("Prendre mon billet de train")
Task.afficherTODO(Task)

train.ordre = 1
Task.afficherTODO(Task)

trainRetour=Task("Prendre un billet retour")
trainRetour.ordre = 2
Task.afficherTODO(Task)

Task.supprimerTache(lait)
Task.afficherTODO(Task)

courses=Task("Faire les courses")
Task.afficherTODO(Task)
	