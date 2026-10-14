import pathlib,importlib.util,html
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('build',ROOT/'scripts/build.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
def field(label,name,typ='text',required=False,options=None,wide=False):
    req=' required' if required else '';star=' <span aria-hidden="true">*</span>' if required else '';cl=' class="wide"' if wide else ''
    if options:control=f'<select id="{name}" name="{name}"{req}><option value="">Choose an option</option>'+''.join(f'<option>{html.escape(x)}</option>' for x in options)+'</select>'
    elif typ=='textarea':control=f'<textarea id="{name}" name="{name}" rows="4"{req}></textarea>'
    else:
        number_attrs=' min="0" step="0.5"' if typ=='number' else ''
        control=f'<input id="{name}" name="{name}" type="{typ}"{number_attrs}{req}>'
    return f'<label{cl} for="{name}">{label}{star}{control}</label>'
def acknowledgment(label, name, summary):
    return f'<label class="check wide" for="{name}"><input id="{name}" type="checkbox" name="{name}" data-summary-label="{summary}" required>{label}</label>'

requirements = [
    'Be at least 21 years old.',
    'Hold a Class A CDL with tanker and hazardous materials endorsements.',
    'Have at least one year of Class A driving experience.',
    'Be available to obtain a TWIC card and TSA clearance.',
    'Have a clean DMV report: 0 points in the past 12 months, or no more than 1.5 points in the past 3 years.',
    'Pass a DOT drug test.',
    'Pass a road test.',
    'Be able to perform lifting duties involving 60–80 lbs., with or without reasonable accommodation.',
    'Be willing to work nights, weekends and holidays on a rotating schedule.',
    'Work well with others.'
]
requirements_panel = '<div class="wide driver-requirements"><h3>Driver Requirements</h3><p>Please review these requirements before completing your application.</p><ul>' + ''.join('<li>' + html.escape(item) + '</li>' for item in requirements) + '</ul>' + acknowledgment('I have reviewed and understand the driver requirements above.', 'requirements_ack', 'Driver Requirements') + '</div>'
yes=['Yes','No']
sections=[]
sections.append(('Your details','Let’s start with how to reach you.',requirements_panel+field('Are you at least 21 years old?','age_21',required=True,options=yes)+field('First name','first','text',True)+field('Last name','last','text',True)+field('Middle initial','middle')+field('Email address','email','email',True)+field('Phone number','phone','tel',True)+field('Street address','address','text',True)+field('Apartment or unit','unit')+field('City','city','text',True)+field('State','state','text',True)+field('ZIP code','zip','text',True)+field('Date available','available','date',True)+field('Desired pay','pay')+field('Preferred location','location',required=True,options=['Ukiah','Bay Area','Sacramento','Any location'])+field('Preferred shift and availability','shift','textarea',True,wide=True)+field('Are you willing to work nights, weekends and holidays on a rotating schedule?','rotating_schedule',required=True,options=yes,wide=True)+field('Are you willing to work cooperatively with other team members?','teamwork',required=True,options=yes,wide=True)+field('Authorized to work in the United States?','work_authorization',required=True,options=yes)+field('Previously employed by Rinehart?','previous_employee',required=True,options=yes)+field('Previously applied to Rinehart?','previous_applicant',required=True,options=yes)+field('Prior employment or application details, if applicable','previous_details','textarea',wide=True)+field('How did you hear about us?','referral')))
sections.append(('License & qualifications','Tell us about your CDL and the credentials you bring.',field('CDL class (Class A required)','cdl',required=True,options=['Class A','Class B','Other'])+field('Issuing state','license_state','text',True)+field('License expiration date','license_expires','date',True)+field('Tanker endorsement?','tanker',required=True,options=yes)+field('Hazardous materials endorsement?','hazmat',required=True,options=yes)+field('TWIC card?','twic',required=True,options=['Yes','No','In progress'])+field('If needed, are you willing and available to obtain a TWIC card and TSA clearance?','twic_tsa_available',required=True,options=['Yes','No','I already hold a TWIC card and TSA clearance'],wide=True)+field('Other licenses held during the past three years, states and expiration dates','prior_licenses','textarea',wide=True)+field('Have you ever been denied a license or driving privilege?','denied',required=True,options=yes)+field('Has a license or driving privilege ever been suspended or revoked?','suspended',required=True,options=yes)+field('Have you ever been disqualified for federal motor carrier safety violations?','disqualified',required=True,options=yes)+field('Explain any Yes answers above','license_explanation','textarea',wide=True)+'<p class="wide form-note">The final secure application will include the driver identification fields from the source PDF. Social Security numbers, date of birth and license numbers are excluded from this public design preview.</p>'))
sections.append(('Driving experience','Show us the experience behind your next mile.',field('Do you have at least one year of Class A driving experience?','class_a_one_year',required=True,options=yes,wide=True)+field('Can you perform the job’s lifting duties involving 60–80 lbs., with or without reasonable accommodation?','lifting_duties',required=True,options=yes,wide=True)+field('Class 6 equipment, dates and approximate miles','class6','textarea')+field('Class 7 equipment, dates and approximate miles','class7','textarea')+field('Class 8 equipment, dates and approximate miles','class8','textarea',True)+field('Other equipment and experience','other_equipment','textarea')+field('States operated in during the past five years','states_driven','textarea',True,wide=True)+field('Special courses, training and safe-driving awards','training','textarea',wide=True)+field('Additional technical skills or special equipment','skills','textarea',wide=True)))
sections.append(('Safety history','Add details where applicable. Enter “None” when there is nothing to report.','<p class="wide form-note">DMV requirement: 0 points in the past 12 months, or no more than 1.5 points in the past 3 years. Enter 0 if you have no points.</p>'+field('DMV points in the past 12 months','dmv_points_12_months','number',True)+field('DMV points in the past 3 years','dmv_points_3_years','number',True)+acknowledgment('I understand that passing a DOT drug test is a requirement for this driving role.','dot_drug_test_ack','DOT Drug Test Requirement')+acknowledgment('I understand that passing a road test is a requirement for this driving role.','road_test_ack','Road Test Requirement')+field('Accidents during the past 10 years: date, nature, fatalities and injuries','accidents','textarea',True,wide=True)+field('Traffic convictions or forfeitures during the past 7 years, excluding parking: location, date, charge and penalty','convictions','textarea',True,wide=True)+field('In the past two years, did a positive pre-employment drug or alcohol test result in not being offered a safety-sensitive transportation position?','positive_test',required=True,options=yes,wide=True)+field('In the past two years, did refusing a pre-employment drug or alcohol test result in not being offered a safety-sensitive transportation position?','refused_test',required=True,options=yes,wide=True)+field('Additional explanation, if needed','safety_details','textarea',wide=True)))
employment='<p class="wide form-note">List all employment during the past three years and commercial driving employment for the preceding seven years, most recent first. Include gaps and military service where relevant.</p>'
employment+='<div id="employers" class="wide">'+''.join(f'<fieldset class="employer"><legend>Employer {i}</legend><div class="form-grid">'+field('Company',f'employer_{i}_company','text',i==1)+field('Phone',f'employer_{i}_phone','tel')+field('Address',f'employer_{i}_address')+field('Supervisor',f'employer_{i}_supervisor')+field('Job title',f'employer_{i}_title')+field('From',f'employer_{i}_from','month')+field('To',f'employer_{i}_to','month')+field('May we contact this supervisor?',f'employer_{i}_contact',options=yes)+field('Responsibilities and reason for leaving',f'employer_{i}_details','textarea',wide=True)+'</div></fieldset>' for i in range(1,4))+'</div><button type="button" id="add-employer" class="secondary-button">+ Add another employer</button>'
employment+=field('Explain employment gaps, if any','gaps','textarea',wide=True)+field('Have you ever been terminated from employment?','terminated',required=True,options=yes)+field('Details, if applicable','terminated_details','textarea',wide=True)
sections.append(('Work history','Your experience matters. Give us the complete picture.',employment))
education=field('Education: school, location, dates, graduation and degree','education','textarea',wide=True)+field('Military service, if applicable: branch, dates, rank and discharge','military','textarea',wide=True)
education+=''.join(f'<fieldset class="wide employer"><legend>Professional reference {i}</legend><div class="form-grid">'+field('Full name',f'reference_{i}_name')+field('Relationship',f'reference_{i}_relationship')+field('Company',f'reference_{i}_company')+field('Phone',f'reference_{i}_phone','tel')+field('Address',f'reference_{i}_address',wide=True)+'</div></fieldset>' for i in range(1,4))
sections.append(('Education & references','People and experience that help tell your story.',education))
sections.append(('Review & acknowledgment','Check your information before the final step.','<div id="application-summary" class="wide summary"></div><label class="check wide"><input type="checkbox" name="accuracy" required>I confirm that the information I provided is accurate to the best of my knowledge.</label><label class="check wide"><input type="checkbox" name="preview_ack" required>I understand this is a design preview. My application has not been sent to Rinehart Oil.</label>'+field('Typed name','signature','text',True)+field('Date','signed_date','date',True)+'<p class="wide form-note">Final employment authorizations and electronic signature wording will be reviewed by Rinehart HR before live applications are enabled. The <a href="../assets/13571-driver-application-with-desc-2019-rev.pdf">original driver application and job description</a> remain available.</p>'))
steps=''.join(f'<section class="application-step" data-step="{i}" '+('' if i==0 else 'hidden')+f'><p class="eyebrow">STEP {i+1} OF {len(sections)}</p><h2>{title}</h2><p class="step-intro">{intro}</p><div class="form-grid">{fields}</div></section>' for i,(title,intro,fields) in enumerate(sections))
body='<section class="page-head wrap"><p class="eyebrow">CAREERS / PETROLEUM TRANSPORTATION DRIVER</p><h1 class="page-title">Your next mile<br>starts here.</h1><p>Apply to drive with a family-owned team built on safe, dependable service.</p></section><section class="page-content wrap"><div class="application-shell"><aside class="application-aside"><img src="../assets/owner-08.webp" alt="Chrome grille of a Rinehart Oil Peterbilt truck"><h2>A team worth<br>driving for.</h2><p>Professional drivers. Company-owned equipment. Real people behind you.</p><a href="../employment-opportunities/index.html">See the driver role </a><p class="form-note">Questions? Call (707) 462-8811.</p></aside><div class="application-main"><div class="notice"><strong>Online application design preview</strong><p>Test the application with sample information. Nothing is sent or saved to a server. Delivery and final HR requirements are being configured.</p></div><div class="progress-label"><span id="step-name">Your details</span><span id="step-count">1 / 7</span></div><progress id="application-progress" max="7" value="1" aria-label="Application progress"></progress><form id="driver-application" novalidate>'+steps+'<div id="form-error" role="alert" tabindex="-1"></div><div class="form-actions"><button type="button" class="secondary-button" id="previous" hidden> Back</button><button type="button" class="button" id="next">Continue </button><button type="submit" class="button" id="finish" hidden>Finish preview</button></div></form><div id="complete" hidden role="status"><h2>Preview complete.</h2><p>Your application has not been submitted. Live delivery is awaiting configuration and HR review.</p><button type="button" class="secondary-button" id="print-application">Print your answers</button><button type="button" class="secondary-button" id="restart">Return to your answers</button></div></div></div></section><script defer src="../assets/application.js?v=20261014-requirements"></script>'
dest=ROOT/'driver-application';dest.mkdir(exist_ok=True);(dest/'index.html').write_text(b.shell('Driver application','/driver-application/',body,'../'),encoding='utf8')
for file in ROOT.rglob('*.html'):
    if any(part in {'scripts','source','templates','.deps'} for part in file.relative_to(ROOT).parts):continue
    prefix='../'*(len(file.relative_to(ROOT).parts)-1);text=file.read_text(encoding='utf8')
    text=text.replace('Customer connections</h3>','Customer connections</h3><a href="'+prefix+'driver-application/index.html">Apply to drive online</a>')
    if file.parent.name=='employment-opportunities':
        target='<div class="source-page-layout">' if '<div class="source-page-layout">' in text else '<div class="prose">'
        text=text.replace(target,'<a class="button application-cta application-image-button" href="'+prefix+'driver-application/index.html" aria-label="Start The Online Driver Application"><img src="'+prefix+'assets/talk-to-rinehart.jpg" alt="Talk To Rinehart" width="488" height="141" loading="lazy" decoding="async"></a>'+target)
    file.write_text(text,encoding='utf8')
import re
for file in ROOT.rglob('*.html'):
    if any(part in {'scripts','source','templates','.deps'} for part in file.relative_to(ROOT).parts):continue
    soup=b.BeautifulSoup(file.read_text(encoding='utf8'),'html.parser')
    for heading in soup.select('title,h1,h2,h3,h4,legend,nav a,.hero-lead,#step-name'):
        for text in list(heading.find_all(string=True)):
            text.replace_with(re.sub(r"(?<![\w'’])([a-z])",lambda m:m.group(1).upper(),str(text)))
    file.write_text(str(soup),encoding='utf8')
print('Built seven-step driver application preview; all page titles and headings use owner-requested Title Case')

from remaining_layout import apply as apply_remaining_layout
apply_remaining_layout(ROOT)

from compact_layout import apply as apply_compact_layout
apply_compact_layout(ROOT)

from strip_arrows import apply as strip_link_arrows
strip_link_arrows(ROOT)

from apply_colophon import apply as apply_site_colophon
apply_site_colophon(ROOT)

from check_release_links import check as check_release_links
check_release_links(ROOT)
