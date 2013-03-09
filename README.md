WebpageLinkParser
=================
Settings.json:    
```   
	{
	    "www.vg.no": { 
	        "links": [
	            "www.vg.no",
	            "vg.no"],
	        "tags": [
	            "/sport/*",
	            "/innenriks"]
	        },
	    "www.nettavisen.no": {
	        "links": [
	            "www.nettavisen.no",
	            "nettaivsen.no"],
	        "tags": []
	    },
	    "www.side3.no": {
	        "links" : [
	            "www.side3.no",
	            "side3.no"],
	        "tags": []
	    }
	}
```   
Her ser du strukturen på fila. Du kan legge til en hoved avis, dette er sia du skal søke på. pass på at du har med `www` og ikke `http://`.
I `links` legger du til avisene du godtar for å telle tags med. Du kan ha f.eks vektklubben sine tags om du så ønsker det. sidene må legges inn med både `www.<nettside>.no` og `<nettside>.no`.
`tags` er en svarteliste med ting du IKKE vil ha med. Skal du ikke ha med noen sports artikkler, legger du til `/sport/*`, stjerna betyr at du ikke skal ha med noe som inneholder den taggen. Skal du ikke ha noen tags som bare er /innenriks, så legger du til `/innenriks`.

Sider som side3.no har nettsider som:
`http://www.side3.no/article3584246.ece`.
Siden den ikke inneholder tags, så vill du bare få ned hele linken og antallet.

vg.no f.eks har:
`http://www.vg.no/sport/ski/langrenn/artikkel.php?artid=10101260`.
Resultate her vill bli `/sport/ski/langrenn`, og den vil legge til 1 for hver artikkel som matcher med hele linken.

Om du skulle ha en mappe med html sider som tillhører vg. Så kan dette legges i en mappe som heter `www.vg.no`, tilsvarer med nettsiden du la til i settings.json. Programmet vil se etter tilsvarende mapper og spørre om du vill gå igjennom dem.


I programmet, som startes med run.py. Så vill du få en meny med valg 1,2,3 osv.
Si du tar 1, som er www.vg.no, så vil programmet først se etter mappa `www.vg.no`. Om den ikke er der vil den bare sjekke nettsia. Er mappa der så vil du bli spurt om du vil sjekke den, du svarer da med enten y (yes) eller n (no).

Etter du har søkt igjennom en side, så har du to valg.
Du kan lagre settings fila og resultatene i noe som heter `session`, eller lagre resultate i csv (kan åpnes i program som excel), eller txt.

Sessions er et lite system som gjør det mulig å lagre resultater, og settings.
`session save` vil lagre dine resultater og settings.
For å finne igjen denne kan du skrive `session list`, den nyeste vil ha et høyere tall, dato står også oppført.
`session restore x` (hvor x er et tall fra session list) vil gjenopprette de gamle filene, du må huske å lagre det du holdt på med først.
Om du gjør forandringer kan du lagre den nye infoen med `session save x`, hvor x er tallet du brukte i restore.

Velger du å lagre fila så kan du skrive `save <navn> <format>`. Alle filene lagres i `saved`
  
Eksempler:  
`save navn`   
lagrer resultate i `navn.txt`  
  
`save txt`   
lagrer resultate med datoen idag og .txt  
  
`save csv`   
lagrer resultate med datoen idag og .csv  
  
`save test csv`   
lagrer resultatet som `test.csv`  
  
Spørsmål kan rettes til:  
mcfoxax@gmail.com 

