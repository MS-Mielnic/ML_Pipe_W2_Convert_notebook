def create_graph(dft):
    # single-value selection to create a dropdown
    # selection1 = alt.selection_single(
    #     name='Select',
    #     fields=['Telemetry Feature Category'],
    #     #init={'Telemetry Feature Category': 'Hash Algorithms'},
    #     bind={'Telemetry Feature Category': alt.binding_select(options=categories)}
    # )
    
    #Binding selectiont to category legend
    selec_leg = alt.selection_point(fields=['Telemetry Feature Category'], bind='legend')

    #Selecting from key and values related to the status of the sub category
    selec_keys=alt.selection_point(fields=['value'])
    #facet chart
    multi=[]
    chart=alt.Chart(dft).mark_square(size=200,opacity=1).encode(
        alt.X('value:N', title=None),
        alt.Y('Sub-Category:N'),
        color='Telemetry Feature Category:N',
        tooltip='Telemetry Feature Category:N',
        opacity=alt.condition(selec_leg, alt.value(0.75), alt.value(0.05))).add_params(selec_leg,selec_keys).transform_filter(selec_leg&selec_keys)


    keys=alt.Chart(new_df_legend).mark_text(
    ).encode(y=alt.Y('keys:N', title=None),text='value:N').add_params(selec_keys).transform_filter(selec_leg
    )


    result=(chart).facet(facet=alt.Facet('product:N', title=None, header=alt.Header(labelFontSize=15
            ))).properties(
        title={'text':['Compare products by sub-category'],
            'subtitle': ['Select in Legend by Status and Telemetry Feature Category', ' ']})
        # title='Comparing products by sub-category. Select in Legend to compare Telemetry Feature Categories'
    #create chart
    inter_result=(result|keys).configure_axis(
        grid=False
    ).configure_view(
        stroke=None
    ).configure_title(fontSize=20)
    return inter_result
    