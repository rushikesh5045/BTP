import re
import networkx as nx


with open("symptoms.txt", "r") as file:
    symptoms = [symptom.strip() for symptom in file.readlines()]

with open("treatment.txt", "r") as file:
    treatments = [treatment.strip() for treatment in file.readlines()]


def find_partial_matches(text, keywords):
    matches = []
    for keyword in keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', text, re.IGNORECASE):
            matches.append(keyword)
    return matches


data = """
glaucoma clinic note glaucoma diagnosis referred glaucoma od os hpi 82 y.o female 3 month follow saw dr. recently says iop good vision seems overall need keep pfats restasis due dryness wants use optive day due glaucoma drops causing irritation right eye reports good compliance drops told needs procedures eyes fine go forward denies eye pain today md hpi stable vision/eyes ou complaints eye medications brimonidine 2x/day od 6:00am dorzolamide 2x/day od 6:30am latanoprost qhs ou 10:00pm restasis 2x/day ou pf ats prn ou current medication list name sig acetaminophen 500 mg tablet take 2 tablets mouth every eight hours needed moderate pain albuterol sulfate hfa 90 mcg/actuation aerosol inhaler inhale 2 puffs mouth every four hours needed amoxicillin 500 mg capsule take 1 capsule mouth three times daily gone atorvastatin 80 mg tablet take 1 tablet daily brimonidine 0.2 eye drops instill 1 drop right eye twice day open glaucoma calcium 600 oral take 1 tablet mouth daily chlorhexidine gluconate 0.12 mouthwash take 10 ml mouth two times daily directed cholecalciferol vitamin d3 1,000 unit tablet take 2,000 units mouth daily ciclopirox 8 topical solution apply adjacent skin affected nails daily remove alcohol every 7 days cyclosporine 0.05 eye drops instill 1 drop eyes two times daily indications dry eye keratoconjunctivitis sicca dorzolamide 2 eye drops instill 1 drop right eye two times daily ferrous sulfate 325 mg 65 mg iron tablet take 325 mg mouth daily fluoxetine 20 mg capsule take 1 capsule daily major depressive disorder oral take 1 tablet mouth daily latanoprost 0.005 eye drops instill 1-2 drops eyes daily bedtime centrum silver oral take 1 tablet mouth daily fish oil oral take mouth glaucoma summary referred 2015 age 78 pseudoexfoliation glaucoma od os without noticeable vision loss ocular diagnoses pseudophakia od cataract os kcn ou uveitis ocular procedures od os phaco/iol slt st none od 26 unknown pachymetry target iop 12 21 diurnal none none glaucoma medications avoid bbs asthma family history glaucoma half-sister oht drops history eye trauma diabetes asthma/copd yes asthma better lately hypotension/ history migraines/raynauds steroid use yes- fluticasone kidney stones driving yes day flomax use never anticoagulation yes- asa 81mg daily occupation msn/health administrator review systems significant ophthalmic symptoms per hpi 12 review systems including constitutional symptoms ent cardiovascular respiratory gastrointestinal genitourinary neurologic psychiatric endocrine hematologic immunologic negative except eye symptoms allergies patient known allergies examination mental status alert oriented x 3 vasc sc vacc cc od 20/40-2 20/30-2 os 20/20-3 motility ortho primary gaze full ou slit lamp exam iop od 12 os 10 applanation 2:46 pm right left gonioscopy +ptm +ptm lids lashes low meniscus poor tear film low meniscus poor tear film conjunctiva sclera quiet quiet senile plaque nasally cornea mild paracentral ant stromal scar layers clear anterior chamber deep quiet deep quiet pxf material iris rr midperipheral surgical changes pxf material iris dilated lens pciol trace pco pxf material lens nsc 1+ conjunctiva includes bulbar palpebral unless otherwise noted cornea includes epithelium stroma endothelium unless otherwise noted fundus exam right left disc cupped flat heme sup inf thin 0.9 thin rim small nerve 0.7 macula erm appears flat flat vitreous +pvd pvd periphery visual h40.1413 pseudoexfoliation glaucoma right eye severe stage h40.1421 pseudoexfoliation glaucoma left eye mild stage .13 cataract nuclear sclerotic eyes assessment plan 1 pseudoexfoliation glaucoma od os mmt s/p slt od iop within target ou planned od iop appears stabilized improvement uveitic control hold surgical intervention time 2 cataract os followed dr. 3 keratoconus ou followed dr. 4 dry eyes followed dr. 5 hx anterior uveitis previously seen dr. missed follow continue drops rtc 6 months hvf 24-2 ou dfe md ophthalmology glaucoma service
chief complaint patient presents follow-up visit 5 months follow primary open angle glaucoma hx carpel tunnel wrist got back california eye meds cosopt 2x-both eyes lumigan night-right eye restasis 2x-both eyes started drops today 9:15am exam base exam visual acuity linear right left dist cc 20/25-1+2 20/30-2 dist ph cc 20/20-1 20/20-2 correction glasses tonometry applanation 1:01 pm right left pressure 16 13 slit lamp fundus exam external exam right left external normal normal slit lamp exam right left lids/lashes normal normal conjunctiva/sclera quiet temporal bleb low somewhat focal cornea layers clear layers clear suture ok anterior chamber deep quiet clear normal normal lens 2+ nsc pciol vitreous normal normal fundus exam right left disc normal heme erosion inferior undermining heme c/d ratio 0.5 macula normal normal vessels normal normal performed reviewed revised history medications allergies well performed elements noted base ophthalmology exam visual acuity pupils normal reaction apd specialty comments pseudophakia os s/p phaco/iol 18.0 sutured wound due trab allergy little used cohesive iop noted 25 2003 alt os 2009 brimonidine eye redness trabeculectomy 0.3 mg/ml mmc 1.5 min left eye imp primary open angle glaucoma severe os pre perimetric od plan optic nerve technician documentation right eye reliability borderline left eye reliability borderline notes optical coherence tomography interpretation hx pt past history primary open angle glaucoma examination good quality scans reveal od 119 112 respectively os values 98 71 result shows thinning inferiorly os particular ongoing followup technique indicated cosopt 2x-both eyes lumigan night-right eye rnfl today shows thinning os particular mild thinning od within normal range follow m.d
"""



patient_graph = nx.Graph()


for conversation in data.split('\n\n'):
    patient_id_match = re.search(r'(\d+) y\.o female', conversation)
    if patient_id_match:
        patient_id = patient_id_match.group(1)

        mentioned_symptoms = find_partial_matches(conversation, symptoms)
        mentioned_treatments = find_partial_matches(conversation, treatments)

        patient_graph.add_node(patient_id, type="patient")

        for symptom in mentioned_symptoms:
            patient_graph.add_node(symptom, type="symptom")
            patient_graph.add_edge(patient_id, symptom, relation="HAS_SYMPTOMS")

        for treatment in mentioned_treatments:
            patient_graph.add_node(treatment, type="treatment")
            patient_graph.add_edge(patient_id, treatment, relation="RECEIVES_TREATMENT")


nx.write_graphml(patient_graph, "patient_graph.graphml")
