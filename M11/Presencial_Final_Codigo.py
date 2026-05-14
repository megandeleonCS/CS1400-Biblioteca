import re
class Pomodoro:
 def _init_(self):
  self.tareas=[]
  self.activo=False
 def validar(self,n):
  return bool(re.match(r"^[A-Za-z ]+$",n))
 def agregar(self,n,p):
  if not hasattr(self,"tareas"):self.tareas=[]
  if not self.validar(n):return "Nombre inválido"
  if p not in ["Alta","Media","Baja"]:return "Prioridad inválida"
  t={"nombre":n,"prio":p,"done":False}
  self.tareas.append(t)
  return "Agregado"
 def buscar(self,n):
  for t in self.tareas:
   if t["nombre"]==n:return t
  return None
 def iniciar(self,i,m):
  if not hasattr(self,"tareas"):self.tareas=[]
  if i>=len(self.tareas):return "Error tarea"
  if m<=0:return "Tiempo inválido"
  self.activo=True
  tiempo=m
  while tiempo>0 and self.activo:
   tiempo-=1
  if tiempo==0:
   self.tareas[i]["done"]=True
   return "Recompensa"
  else:
   return "Pausado"
 def pausar(self):
  if self.activo:
   self.activo=False
   return "Pausado"
  else:
   return "No activo"
 def resumen(self):
  total=0
  hechas=0
  for t in self.tareas:
   total+=1
   if t["done"]:hechas+=1
  return {"total":total,"hechas":hechas}
p=Pomodoro()
print(p.agregar("Estudiar","Alta"))
print(p.agregar("Leer","Media"))
print(p.iniciar(0,2))
print(p.resumen())