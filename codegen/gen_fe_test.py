import gen_utils
u = gen_utils
uc = u.CHARS
dprint = u.dprint

#kam pani garos, with this Model, code also runs
template_path=f'bepyMaster/mainProject/templates/{uc.place_model}/{uc.place_model}Test.js'
file_sample_template_content=open(template_path,"r").read()
tab='    '

def GetS2(**k):
    c = k.get('current_column_obj')
    s=""
    dprint(c)

    col_name=c.name
    if c.fe_gql_name: #bank_id changes to bankId
        col_name=c.fe_gql_name

    if c.type=='int':
       # bank_id: 99,
        s = f"""{col_name}:99,"""
    elif c.type=='char':     
        # name: "test1",
        s = f"""{col_name}:"char","""
    else:
        s = f"add extra to codegen"
    
    if c.pk:
        s = f"""{col_name}:"","""
    
    s = f"{uc.tab1}{s}{uc.nl}"
    return s


def GetCode(**kwargs):
    model= kwargs.get('model')
    content=file_sample_template_content

    content=u.GenPlaceholderSrc(
        model=model,
        orgSrc=content,
        placeholder = uc.place_jc1,
        fnCallback = GetS2
    )

    content=u.GenPlaceholderSrc(
        model=model,
        orgSrc=content,
        placeholder = uc.place_jc2,
        fnCallback = GetS2
    )
    
    content = content.replace(uc.place_model, model.name)
    content = content.replace(uc.place_model_gql, model.name_gql)
    return content

def write_code(**kwargs):
    model=kwargs.get('model')
    model_name = model.get('name')
    out_dir = f'{uc.out_loc_prefix}bepyMaster/mainProject/mainApp/templates/{model_name}'
    dprint(out_dir)

    import os
    os.makedirs(out_dir,exist_ok=True)

    str_model_content = GetCode(model=model)
    dprint(str_model_content)

    out_file=f'{out_dir}/{model_name}Test.js'
    f = open(out_file,'w')
    f.write(str_model_content)
    f.close()
    
    pass

if __name__ == '__main__':
    write_code(model=model)
    pass 


