"""Overlay printable AcroForm fields without rewriting the original agreement."""
from pathlib import Path
import json
from pypdf import PdfReader, PdfWriter
from pypdf.generic import (DictionaryObject, NameObject, ArrayObject, NumberObject,
    FloatObject, TextStringObject, BooleanObject, DecodedStreamObject)
ROOT=Path(__file__).resolve().parents[1]
WORK=Path(r'C:\Users\Admin\OneDrive - CWU\AI\Projects\Rinehart-Oil-Website-Redesign-Content-Migration\credit-fillable')
w=PdfWriter();w.clone_document_from_reader(PdfReader(WORK/'original-credit-packet.pdf'))
font=w._add_object(DictionaryObject({NameObject('/Type'):NameObject('/Font'),NameObject('/Subtype'):NameObject('/Type1'),NameObject('/BaseFont'):NameObject('/Helvetica'),NameObject('/Encoding'):NameObject('/WinAnsiEncoding')}))
fields=ArrayObject();form=DictionaryObject({NameObject('/Fields'):fields,NameObject('/DR'):DictionaryObject({NameObject('/Font'):DictionaryObject({NameObject('/Helv'):font})}),NameObject('/DA'):TextStringObject('/Helv 0 Tf 0 g'),NameObject('/NeedAppearances'):BooleanObject(False)})
w.root_object[NameObject('/AcroForm')]=w._add_object(form)
manifest=[]
def add(page,name,x,top,width,height=12,checkbox=False,multiline=False):
    name=f'p{page}_{name}';rect=[x,842-top-height,x+width,842-top]
    a=DictionaryObject({NameObject('/Type'):NameObject('/Annot'),NameObject('/Subtype'):NameObject('/Widget'),NameObject('/FT'):NameObject('/Btn' if checkbox else '/Tx'),NameObject('/T'):TextStringObject(name),NameObject('/TU'):TextStringObject(name.replace('_',' ')),NameObject('/Rect'):ArrayObject([FloatObject(n) for n in rect]),NameObject('/F'):NumberObject(4),NameObject('/Ff'):NumberObject(4096 if multiline else 0),NameObject('/P'):w.pages[page-1].indirect_reference,NameObject('/DA'):TextStringObject('/Helv 0 Tf 0 g'),NameObject('/BS'):DictionaryObject({NameObject('/W'):NumberObject(0)})})
    if checkbox:
        appearances=DictionaryObject()
        for state,data in [('Off',''),('Yes',f'0 g 1 w 1 1 m {width-1} {height-1} l S 1 {height-1} m {width-1} 1 l S')]:
            st=DecodedStreamObject();st.set_data(data.encode());st.update({NameObject('/Type'):NameObject('/XObject'),NameObject('/Subtype'):NameObject('/Form'),NameObject('/BBox'):ArrayObject([NumberObject(0),NumberObject(0),FloatObject(width),FloatObject(height)]),NameObject('/Resources'):DictionaryObject()});appearances[NameObject('/'+state)]=w._add_object(st)
        a[NameObject('/AP')]=DictionaryObject({NameObject('/N'):appearances});a[NameObject('/V')]=NameObject('/Off');a[NameObject('/AS')]=NameObject('/Off')
    else:a[NameObject('/V')]=TextStringObject('')
    ref=w._add_object(a);fields.append(ref);p=w.pages[page-1];p.setdefault(NameObject('/Annots'),ArrayObject()).append(ref);p[NameObject('/Tabs')]=NameObject('/S')
    manifest.append({'name':name,'page':page,'rect':rect,'type':'checkbox' if checkbox else 'text'})
def row(top,spec,height=11):
    for name,x,end in spec:add(1,name,x,top,end-x,height)
row(105,[('company_name',53,295),('telephone',299,435),('fax',439,566)])
for label,y in [('billing',126.5),('delivery',148)]:row(y,[(label+'_address',53,295),(label+'_city',299,435),(label+'_state',439,505),(label+'_zip',509,566)])
row(169,[('business_description',53,260),('years_in_business',264,388),('hours',392,566)])
for name,x in [('sole_proprietor',174),('general_partnership',260),('limited_partnership',354),('corporation',424),('llc',530)]:add(1,name,x,183,5,5,checkbox=True)
for label,y in [('primary_contact',211.5),('manager',233)]:row(y,[(label+'_name',53,295),(label+'_email',299,435),(label+'_cell',439,566)])
row(254,[('own_or_lease',53,135),('landlord_name',141,268),('landlord_phone',272,374),('bankruptcy_details',378,566)])
for label,top in [('pricing',268),('invoices',282),('draft_notices',296)]:
    for name,x in [('fax',142),('email',217),('station',359),('owner_corporate',455)]+([('mail',281)] if label=='invoices' else []):add(1,label+'_'+name,x,top,5,5,checkbox=True)
row(318,[('diesel_tank_size',128,195),('unleaded_tank_size',200,267),('midgrade_tank_size',271,331),('premium_tank_size',335,566)],9)
for i,y in enumerate([337.5,380,422.5],1):
    row(y,[(f'principal{i}_{n}',x,end) for n,x,end in [('name',53,196),('title',200,266),('ownership_percent',270,332),('ssn',336,428),('drivers_license',432,566)]])
    row(y+21.25,[(f'principal{i}_{n}',x,end) for n,x,end in [('home_address',53,196),('city',200,266),('state',270,303),('zip',308,332),('home_phone',336,428),('birth_date',432,566)]])
for i,y in enumerate([465,486.3,507.5],1):row(y,[(f'officer{i}_{n}',x,end) for n,x,end in [('name',53,197),('address',201,303),('city',308,332),('state',336,358),('zip',363,428),('title',432,566)]])
row(529,[('federal_tax_id',53,303),('sos_corporate_id',308,566)])
for label,y in [('supplier',550),('trade_reference1',592.5),('trade_reference2',635)]:
    row(y,[(label+'_name',53,197),(label+'_contact',201,303),(label+'_account',308,566)])
    row(y+21.25,[(label+'_'+n,x,end) for n,x,end in [('address',53,195),('city',199,266),('state',270,302),('zip',306,329),('phone',333,427),('fax',431,566)]])
row(677.5,[('bank_name',53,330),('bank_contact',335,566)])
row(699,[(f'bank_{n}',x,end) for n,x,end in [('address',53,195),('city',199,266),('state',270,302),('zip',306,329),('phone',333,427),('fax',431,566)]])
row(720,[('checking_account',53,266),('savings_account',270,566)])
row(741.5,[('credit_amount_requested',53,264),('gallons_requested',268,566)],10)
add(2,'seller_permit',370,71,170,18)
for name,x,t,width,h in [('signature',74,746,310,14),('title',400,746,88,14),('date',508,746,49,14),('printed_name',74,769,310,14)]:add(2,name,x,t,width,h)
for i,t in enumerate([726,751],1):
    for n,x,width in [('guarantor_signature',108,132),('spouse_signature',305,129),('date',458,47)]:add(3,f'{n}{i}',x,t,width,15)
add(4,'customer_name',53,146,105,15)
for who,y in [('creditor',652),('customer',706.5)]:
    for n,x,width in [('day',98,33),('month',159,53),('year',217,49)]:add(4,who+'_'+n,x,y,width,15)
    add(4,who+'_signature',132,y+27.5,166,15);add(4,who+'_printed_name',356,y+27.5,168,15)
add(5,'account_name',123,160,216,14);add(5,'account_number',136,188,203,14)
for label,x,end in [('station',154,339),('owner_corporate',394,564)]:
    for name,y in [('street',241),('city_zip',265),('phone',289),('fax',314),('cell',338),('email',362),('hours',387),('manager',411)]:add(5,label+'_'+name,x,y,end-x,14)
for name,y in [('premium',456),('unleaded',471),('midgrade',486),('diesel',501)]:
    add(5,name+'_available',172,y+1,10,10,checkbox=True);add(5,name+'_tank_size',246,y,92,13)
for label,y in [('pricing',559),('invoices',573.2),('draft_notices',587.4)]:
    for n,x in [('station',211),('owner_corp',320),('fax',402),('email',547)]+([('mail',474)] if label!='draft_notices' else []):add(5,label+'_'+n,x,y+1,10,10,checkbox=True)
add(5,'office_date_opened',154,636,91,13)
for n,x,y in [('factor',320,637),('banking',402,637),('files',472,637),('payment_cod',211,657),('payment_eft',320,657),('payment_fax_check',402,657),('station_branded',211,686),('station_unbranded',320,686),('station_frt_mile',402,686)]:add(5,'office_'+n,x,y,10,10,checkbox=True)
for n,x,y,width,h in [('forms',465,657,74,13),('terminal',495,685,67,13),('terminal_fee',154,699,91,13),('notes',76,719,484,24)]:add(5,'office_'+n,x,y,width,h,multiline=n=='notes')
for n,x,y,width,h in [('business_name',53,164,305,15),('telephone',366,164,160,15),('address',53,194,155,15),('city',214,194,112,15),('state',333,194,98,15),('zip',438,194,88,15),('authorizing_name',53,238,205,15),('bank_name',108,298,191,16),('branch',338,298,196,16),('bank_city',75,328,228,16),('bank_state',333,328,94,16),('bank_zip',446,328,84,16),('routing_number',136,358,164,16),('bank_account',347,358,186,16),('bank_telephone',101,388,176,16),('checking',327,388,82,16),('savings',450,388,85,16),('authorized_day',135,644,74,16),('authorized_month',247,644,155,16),('authorized_year_suffix',420,644,41,16),('printed_name',53,688,228,18),('signature',290,688,238,18)]:add(6,n,x,y,width,h)
for n,x,y,width,h in [('customer_name',140,184,307,16),('seller_permit',292,229,228,16),('business_products_line1',430,249,89,16),('business_products_line2',53,269,233,15),('date',96,464,105,16),('signature',269,464,274,16),('place',96,499,105,16),('title',269,499,274,16),('phone',96,535,105,16),('address',269,535,274,16)]:add(7,n,x,y,width,h)
for p in w.pages:w.update_page_form_field_values(p,{m['name']:'' for m in manifest if m['type']=='text'},auto_regenerate=False)
w.add_metadata({'/Title':'Rinehart Oil Credit Application Packet, Fillable','/Subject':'Fill, save, print and return the completed packet. Original agreement text preserved.'})
with (ROOT/'assets/6352-roi-credit-packet.pdf').open('wb') as f:w.write(f)
(WORK/'field-manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf8')
print(f'Created seven-page fillable packet with {len(manifest)} fields')
