var myObj = "";
		var allTextLines="";
		var cur_const = "";
		var dict_colors = {
						'BharatiyaJanataParty':'#ff9933',
						'IndianNationalCongress':'#0F6796',
            	   'BahujanMuktiParty':'#ffa500',
            	   'BahujanSamajParty':'#000080',
               	'VyavasthaParivartanParty':'#ffff00',
               	'RealDemocracyParty':'#008000',
               	'Shivsena':'#0000ff',
               	'Independent':'#ff0000',
               	'AamAadmiParty':'#000000',
               	'SamajwadiParty':'#A52A2A',
               	'YuvaSarkar':'#800000',
               	'JanataDal(United)':'#B22222',
               	'AllIndiaHindustanCongressParty':'#8B0000',
               	'RashtriyaKrantikariSamajwadiParty':'#5E3A32',
               	'NationalistCongressParty':'#B8978F',
               	'GujaratJanChetnaParty':'#BEC8D2',
               	'AapniSarkarParty':'#1E3C5C',
               	'BhartiyaTribalParty':'#BB2FAF',
               	'SwabhimanParty':'#60DC19',
               	'RashtriyaSamajwadiParty(Secular)':'#DE1E6A',
               	'LokVikasManch':'#7E295B',
               	'NavinBharatNirmanManch':'#EF0790',
               	'LokGathbandhanParty':'#1B9878',
               	'RepublicanPartyofIndia':'#3574EC',
               	'BharatiyaNationalJantaDal':'#1CEC2F',
               	'BharatiyaRashtravadiPaksha':'#D0E81F',
               	
 		}
		$(document).ready(function() {
    		$.ajax({
        		type: "GET",
        		url: "data/consistituency6.csv",
        		dataType: "text",
        		success: function(data) {processData(data);}
     	}	);
		});

	function processData(allText) {
		allTextLines = allText.split(/\r\n|\n/);
		var headers = allTextLines[0].split(',');
		var lines = [];

		for (var i=1; i<allTextLines.length; i++) {
			var data = allTextLines[i].split(',');
   			if (data.length == headers.length) {
				var tarr = [];
				for (var j=0; j<headers.length; j++) {
      				tarr.push(headers[j]+":"+data[j]);
      			}
      			lines.push(tarr);
			}
		}
   	startPlot();
	}
	function plot(){
		//alert("kkkkkk");
		var x="";
		var candidate=new Array();
		var votes = new Array();
		var party = new Array();
		var col = new Array();
		
		for (x in myObj) {
			
			var vv = myObj[x].split(',');
			//alert(vv);
			if(vv[2]==cur_const){
				//alert(vv);
				vv[1] = vv[1].split('_').join(' ');
				vv[3] = vv[3].split('_').join('');
				candidate.push(vv[1]);
				votes.push(vv[4]);
				party.push(vv[3]);
				col.push(dict_colors[vv[3]]);
			}
		}
		//alert(candidate);
		var v = votes.map(function (x) { 
    		return parseInt(x, 10); 
		});
		
		
		var b = candidate;
		var a = votes;
		var c = new Array();
		for(var i = 0; i < a.length; i++)
		{
    		c.push('Votes: '+a[i]+'<br>Candidate: '+b[i]);
		}
		
		var data = [{
    		x: party,
    		y: v,
    		type: 'bar',
    		
    		text:c,
    		hoverinfo: 'text',
         mode: 'markers',
 			marker: {color: col,opacity:1,}
  		}];
  		layout = {
        hovermode:'closest',
        title:'Visual Report',
        xaxis:{zeroline:false, hoverformat: '.2r'},
        yaxis:{zeroline:false, hoverformat: '.2r'}
     };
  		//$('#myDiv').empty();
		Plotly.newPlot('myDiv', data,layout);
		
		jQuery('#mySelector').html('');
		unique_Win =[];
   	
		$.each(party, function(i, el){
   			if($.inArray(el, unique_Win) === -1) unique_Win.push(el);
		});
		
		var ks = 0;
		var content = "<table><tr>"
		for(var i=0; i<unique_Win.length; i++){
			//alert(unique_Win[i]);
    		content += '&nbsp<td> <div style="height:20px; border:1px solid black; width:20px; background-color:'+dict_colors[unique_Win[i].split('_').join('')]+'"> </div></td><td><b>' +  unique_Win[i].split('_').join(' ') + '</b></td>';
			ks = ks+1;			
			if(ks%3==0){
				content += '</tr><tr>';
			}		
		}
		content += "</tr></table>"

	$('#mySelector').append(content);
	}
	
	function startPlot() {
		var x, txt = "";
		var constitutency = new Array();
		myObj = allTextLines.slice(1,allTextLines.length-1);
		for (x in myObj) {
			vv = myObj[x].split(',');
			constitutency.push(vv[2])
		}
      
   	var uniqueConst = [];
		$.each(constitutency, function(i, el){
   			if($.inArray(el, uniqueConst) === -1) uniqueConst.push(el);
		});
		$('#selectC').empty();
		$.each(uniqueConst, function(i, p) {
   			$('#selectC').append($('<option></option>').val(p).html(p));
		});
		cur_const = uniqueConst[0];
		plot();
	
	}
	
	function constChange(selectC){
		
    	cur_const = selectC.value;
    	plot();
	}
	function stateChange(selectS){
		if (selectS.value=='Gujarath'){
			$.ajax({
        	type: "GET",
        	url: "data/consistituency6.csv",
        	dataType: "text",
        	success: function(data) {processData(data);}
     		});
		}
		if (selectS.value=='HimachalPradesh'){
			$.ajax({
        	type: "GET",
        	url: "data/consistituency8.csv",
        	dataType: "text",
        	success: function(data) {processData(data);}
     		});
		}
	}
