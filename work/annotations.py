def annotate_with_bio(conversation, glaucoma_keywords):
    annotations = []
    words = conversation.split()
    for word in words:
        if word.lower() in glaucoma_keywords:
            annotations.append("B-Glaucoma")
        elif annotations and annotations[-1] == "B-Glaucoma":
            annotations.append("I-Glaucoma")
        else:
            annotations.append("O")
    return annotations

def save_annotations(conversation, annotations, output_file):
    with open(output_file, 'w') as f:
        for word, annotation in zip(conversation.split(), annotations):
            f.write(f"{word}\t{annotation}\n")


with open("./output.txt", 'r') as f:
    conversations = f.readlines()


glaucoma_keywords = {
    "glaucoma", "vision", "drops", "eye", "medications", "ophthalmic", "optic",
    "nerve", "surgery", "visual", "field", "procedure", "retinal", "diagnosis",
    "treatment", "clinic", "diagnosis", "referred", "open-angle", "pseudoexfoliation",
    "trabeculectomy", "cosopt", "lumigan", "restasis", "tonometry", "timolol", "combigan",
    "selective", "laser", "trabeculoplasty", "cataract", "tension",
    "dryness", "pfats", "optive", "compliance", "acetaminophen", "albuterol",
    "amoxicillin", "atorvastatin", "brimonidine", "calcium", "cholecalciferol",
    "ciclopirox", "cyclosporine", "depressive", "centrum", "fish", "pseudoexfoliation",
    "cataract", "keratoconus", "uveitis", "trabeculectomy", "visual", "pseudoexfoliation",
    "nuclear", "sclerotic", "pachymetry", "retinal", "cataract", "fluoxetine",
    "vitamin", "oral", "anticoagulation", "msn/health", "posterior", "capsular",
    "opacification", "varix", "mitomycin", "prednisolone", "neomycin-polymyxin-dexamethasone",
    "calcitriol", "doxazosin", "furosemide", "losartan", "toprol", "lisinopril",
    "trabeculectomy", "mitomycin", "tylenol", "ofloxacin", "acetaminophen",
    "atenolol", "aspirin", "hydrocodone-acetaminophen", "acetate", "trabeculectomy",
    "mitomycin", "prednisolone",
    "Clinic note", "Referred", "POAG (Primary Open-Angle Glaucoma)", "Ocular", "Visual field",
    "Eye pain", "Compliance", "Travatan Z", "ATS (Anti-Tension Suture)", "Eye gel",
    "Glaucoma summary", "Procedures", "IOP (Intraocular Pressure)", "Meibomian gland dysfunction",
    "Latanoprost", "Capsular glaucoma", "Pseudoexfoliation", "Lens", "Tube", "Lubrication",
    "S/P SLT (Selective Laser Trabeculoplasty)", "VF (Visual Field)", "Examination", "Glaucoma suspect",
    "HBP (High Blood Pressure)", "IOP check", "Gonio (Gonioscopy)", "Rib fracture",
    "Thick pachymetry", "RNFL (Retinal Nerve Fiber Layer)", "Laser retinopexy", "Steroid responder",
    "ERM (Epiretinal Membrane)", "Optic neuropathy", "Pachy (Pachymetry)", "Blood pressure medications",
    "Thin pachy", "PAS (Peripheral Anterior Synechiae)", "Sup/inf (Superior/Inferior)", "Bleb",
    "Scribe", "Aortic valve replacement", "Depth perception", "Dizziness", "Newsprint",
    "Way valve replacement", "Peripheral uveitis", "Phthisis", "Macular atrophy",
    "Pigment dispersion syndrome", "Nystagmus", "Aphakic", "Sulcus IOL (Intraocular Lens)",
    "YAG (Yttrium Aluminum Garnet) laser", "Blepharitis", "Myopia", "Glaucoma progression",
    "Psoriasis", "PVD (Posterior Vitreous Detachment)", "Drusen", "HTN (Hypertension)",
    "High myopia", "Thin cornea", "Anterior chamber", "RVF (Retinal Visual Field)",
    "Scleral thinning", "Vitreous", "Glaucoma medication", "Floaters", "Night flashes",
    "CME (Cystoid Macular Edema)", "MS (Multiple Sclerosis)", "Mild cataracts", "Dry AMD (Age-related Macular Degeneration)",
    "Shunt", "Myopia", "Cataract surgery", "Pachymetry", "HVF (Humphrey Visual Field)",
    "OCT (Optical Coherence Tomography)", "Low tension glaucoma", "Steroid responder",
    "Peripheral anterior synechiae (PAS)", "Meibomian gland dysfunction", "Anti-VEGF",
    "Corneal Edema", "Phaco/IOL (Phacoemulsification/Intraocular Lens Implantation)", "Family History",
    "Side Effects", "Corticosteroids", "Adverse Events", "Prednisolone Acetate", "Drug Compliance",
    "Anxiety", "Incisional Surgery", "Diode Laser", "Risks/Benefits", "Adverse Reactions",
    "Open-angle glaucoma", "Thin corneas", "Visual distortion", "Borderline pressure control",
    "Progression noted", "Glaucoma monitor", "Wide-angle glaucoma", "Normotension open angle glaucoma",
    "Early defects", "Superior paracentral defect", "Superior arcuate", "Thin retinas",
    "Glaucomatous appearance", "Pseudoexfoliation", "Visual symptoms", "Eye surgeries",
    "Occupational history", "Contact lens wear", "Asthma/COPD", "Migraines/Raynaud's",
    "Steroid use", "Kidney stones", "Driving", "Flomax use", "Examination", "Treatment plan",
    "Visual field defects", "Ophthalmology clinic", "Dilated fundus exam", "Retinal pathology",
    "Congenital glaucoma",
    "trabeculoplasty", "trabeculectomy", "mitomycin-c", "gonio", "intraocular pressure (IOP)",
    "visual field", "optic nerve", "retinal nerve fiber layer (RNFL)", "macula", "anterior chamber",
    "cataract", "pseudoexfoliation material", "hypotony", "lumigan", "latanoprost", "cosopt",
    "brimonidine", "dorzolamide", "timolol", "prostaglandin analogs", "prostaglandin eye drops"
}


annotated_conversations = []
for conversation in conversations:
    annotations = annotate_with_bio(conversation, glaucoma_keywords)
    annotated_conversations.append(annotations)


output_file = "annotated_output.txt"
with open(output_file, 'w') as f:
    for conversation_annotations in annotated_conversations:
        for word, annotation in zip(conversation.split(), conversation_annotations):
            f.write(f"{word}\t{annotation}\n")
        f.write("\n")

print("Annotations saved to", output_file)
