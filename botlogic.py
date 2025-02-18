import random
def conta():
    elementos = ["Combustibles fósiles (petróleo, gas natural y carbón)",'Plásticos y materiales sintéticos','Metales pesados y minería (oro, cobre, aluminio, etc.)','Agricultura intensiva y ganadería','Mal uso del agua potable','Deforestación y uso insostenible de la madera','Residuos electrónicos (e-waste)']
    return random.choice(elementos)

def no_conta():
    elen = ["Ahorra energía: Usa bombillas LED, apaga luces y desconecta aparatos cuando no los uses.",'Reduce el consumo de agua: Cierra el grifo mientras te cepillas los dientes o lavas los platos.','Recicla y reutiliza: Separa la basura y dale una segunda vida a objetos antes de desecharlos.','Usa productos ecológicos: Evita químicos tóxicos y prefiere opciones biodegradables.','Usa transporte público, bicicleta o camina en vez de usar el coche.','Deforestación y uso insostenible de la madera','Evita plásticos de un solo uso y lleva tu propia bolsa, botella y tupper.',"No tires basura en la calle, playas o montañas.","Planta árboles y cuida las áreas verdes.","Evita el uso de pesticidas y productos contaminantes."]
    return random.choice(elen)


recicla = """♻️ **Objetos Reciclables**

**Plásticos:**  
- Botellas de agua y refrescos (PET)  
- Envases de champú y jabón líquido  
- Bolsas plásticas reutilizables  
- Envases de yogur y crema  
- Tapas de plástico  
- Tuppers plásticos (limpios)  

**Vidrio:**  
- Botellas de vidrio (vino, cerveza, refrescos)  
- Frascos de mermelada y salsas  
- Envases de perfume y cosméticos (sin residuos)  

**Papel y Cartón:**  
- Periódicos y revistas  
- Cajas de cartón limpias  
- Sobres y hojas de papel usadas  
- Cuadernos sin espiral  
- Rollos de papel higiénico y toallas de cocina  

**Metales:**  
- Latas de aluminio (refrescos, cerveza)  
- Latas de conservas (atún, verduras enlatadas)  
- Tapas metálicas de frascos  
- Utensilios de cocina metálicos en buen estado  

**Orgánicos (para compostaje):**  
- Cáscaras de frutas y verduras  
- Restos de café y bolsitas de té  
- Cáscaras de huevo  
- Hojas secas y ramas pequeñas  

**Electrónicos (en centros de reciclaje):**  
- Pilas recargables  
- Teléfonos celulares  
- Computadoras y accesorios  
- Cables y cargadores  
- Electrodomésticos pequeños"""

no_reci = """🚫 **Objetos No Reciclables**

**Plásticos:**  
- Bolsas plásticas de un solo uso  
- Envases de comida contaminados con grasa (ej. bandejas de comida rápida)  
- Envoltorios metalizados (papitas, golosinas)  
- Juguetes plásticos mezclados con otros materiales  

**Vidrio:**  
- Vidrios rotos  
- Espejos  
- Bombillas y focos  
- Vidrio templado (ventanas, parabrisas)  

**Papel y Cartón:**  
- Servilletas y papel higiénico usados  
- Papel encerado o plastificado  
- Cartón de pizza con grasa  
- Fotografías  

**Metales:**  
- Objetos oxidados  
- Aerosoles con residuos peligrosos  
- Cacerolas y sartenes antiadherentes dañadas  

**Orgánicos:**  
- Restos de carne y huesos grandes  
- Lácteos y derivados (queso, leche)  
- Aceites de cocina usados (se deben reciclar en puntos específicos)  

**Electrónicos:**  
- Baterías de un solo uso (difícil reciclaje)  
- Televisores antiguos sin puntos de recolección  
- Bombillas fluorescentes (contienen mercurio)"""

desco = """**Residuos orgánicos (restos de comida):**
Aproximadamente 2 a 6 meses, ideales para compostaje.

**Papel y Cartón:**
El papel puede degradarse en 2 a 6 meses, mientras que el cartón, si se mantiene seco, puede tardar hasta 2 años.

**Plásticos:**
- Botellas de plástico: 450 a 1,000 años.
- Bolsas de plástico: Alrededor de 150 años.
- Otros productos plásticos (juguetes, envases): Entre 300 y 1,000 años.
FUNDACIONAQUAE.ORG

**Vidrio:**
Alrededor de 4,000 años o más, ya que el vidrio no se degrada de forma natural.

**Metales:**
- Latas de aluminio: Aproximadamente 200 años.
- Tapas metálicas: Cerca de 30 años.

**Otros residuos:**
- Pilas: Entre 500 y 1,000 años.
- Madera: La madera natural puede descomponerse en 1 a 5 años; si está tratada o pintada, hasta 12–15 años.
- Chicles: Aproximadamente 5 años.
- Colillas de cigarrillo: Entre 2 y 12 años, según su composición."""
