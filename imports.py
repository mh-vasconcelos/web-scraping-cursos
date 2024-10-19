import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


cursos = '''<div class="js-render-wrapper lw-cols multiple-rows multiple-rows-tl multiple-rows-tp multiple-rows-sl multiple-rows-sp align-items-stretch main ">
		

			
			

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=excel-analytics-com-inteligencia-artificial">
    <a class="lw-course-card--stretched-link" href="/course?courseid=excel-analytics-com-inteligencia-artificial">Excel Analytics com Inteligência Artificial</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/b90653445c75078ec0fcbd5fd62fb88f.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            
            <div class="lw-course-card-ribbon lw-brand-accent1-bg lw-course-card-ribbon-top-right" style="opacity: 1">
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element ellipsis">oferta especial</p>
            </div>
            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">72 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Machine Learning Inteligência Artificial Microsoft Excel
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">72 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Excel Analytics com Inteligência Artificial</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Equipe DSA</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                                <span>You save 23% </span>
                            
                            -->

                            
                                
                                    
                                        <span class="lw-deleted-price v-middle lw-text-color-fadeout50 weglot-exclude">
                                            R$1.299
                                        </span>
                                        <span class="v-middle weglot-exclude">
                                            <strong>R$999</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=excel-analytics-com-inteligencia-artificial" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=fundamentos-de-data-science-e-inteligencia-artificial">
    <a class="lw-course-card--stretched-link" href="/course?courseid=fundamentos-de-data-science-e-inteligencia-artificial">Fundamentos de Data Science e Inteligência Artificial</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/8e1463379566a2fc392d3f4eaa8613cd.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">24 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Gratuito Fundamentos Data Science Inteligência Artificial
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">24 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Fundamentos de Data Science e Inteligência Artificial</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Equipe DSA</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                                <span>You save 29% </span>
                            
                            -->

                            
                                <strong>Gratuito</strong>
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=fundamentos-de-data-science-e-inteligencia-artificial" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=fundamentos-de-engenharia-de-dados">
    <a class="lw-course-card--stretched-link" href="/course?courseid=fundamentos-de-engenharia-de-dados">Fundamentos de Engenharia de Dados</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/9297c9451128e5e2ae8aa71e713f1762.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">24 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Gratuito Engenharia de Dados Fundamentos
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">24 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Fundamentos de Engenharia de Dados</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Equipe DSA</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                                <span>You save 29% </span>
                            
                            -->

                            
                                <strong>Gratuito</strong>
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=fundamentos-de-engenharia-de-dados" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=fundamentos-de-linguagem-python-para-analise-de-dados-e-data-science">
    <a class="lw-course-card--stretched-link" href="/course?courseid=fundamentos-de-linguagem-python-para-analise-de-dados-e-data-science">Fundamentos de Linguagem Python Para Análise de Dados e Data Science</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/7872b73546ba050740eceb16c62e6916.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">72 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Gratuito Fundamentos Linguagem Python Analytics
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">72 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Fundamentos de Linguagem Python Para Análise de Dados e Data Science</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Equipe DSA</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                                <span>You save 29% </span>
                            
                            -->

                            
                                <strong>Gratuito</strong>
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=fundamentos-de-linguagem-python-para-analise-de-dados-e-data-science" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=analise-e-previsao-de-series-temporais-com-inteligencia-artificial">
    <a class="lw-course-card--stretched-link" href="/course?courseid=analise-e-previsao-de-series-temporais-com-inteligencia-artificial">Análise e Previsão de Séries Temporais com Inteligência Artificial</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/c705a57a26bebc1a19d73da5892ed02d.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">72 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Séries Temporais Forecasting Inteligência Artificial Linguagem Python Transformers Estatística Deep Learning Real-Time Analytics
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">72 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Análise e Previsão de Séries Temporais com Inteligência Artificial</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Equipe DSA</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.449</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=analise-e-previsao-de-series-temporais-com-inteligencia-artificial" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=aplicacoes-de-large-language-models-llms-na-area-medica">
    <a class="lw-course-card--stretched-link" href="/course?courseid=aplicacoes-de-large-language-models-llms-na-area-medica">Aplicações de Large Language Models (LLMs) na Área Médica</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/662fab26668aff49eee3a4f130796ef8.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">90 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Processamento de Linguagem Natural Inteligência Artificial Large Language Models (LLMs)
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">90 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Aplicações de Large Language Models (LLMs) na Área Médica</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.870</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=aplicacoes-de-large-language-models-llms-na-area-medica" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=armazenamento-e-gestao-de-dados-com-data-lake-e-data-lakehouse">
    <a class="lw-course-card--stretched-link" href="/course?courseid=armazenamento-e-gestao-de-dados-com-data-lake-e-data-lakehouse">Armazenamento e Gestão de Dados com Data Lake e Data Lakehouse</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/1e52b46d9d0e3fd9e91661016162b1f0.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">86 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Data Lakehouse Data Lake Databricks Linhagem de Dados Data Quality Alteryx
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">86 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Armazenamento e Gestão de Dados com Data Lake e Data Lakehouse</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.530</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=armazenamento-e-gestao-de-dados-com-data-lake-e-data-lakehouse" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=arquitetura-de-plataforma-de-dados-e-modern-data-stack">
    <a class="lw-course-card--stretched-link" href="/course?courseid=arquitetura-de-plataforma-de-dados-e-modern-data-stack">Arquitetura de Plataforma de Dados e Modern Data Stack</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/2e356a4b32abfb78afd23326cf54a55d.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">96 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Modern Data Stack Arquitetura de Dados Plataforma de Dados
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">96 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Arquitetura de Plataforma de Dados e Modern Data Stack</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.340</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=arquitetura-de-plataforma-de-dados-e-modern-data-stack" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=automacao-robotica-de-processos-com-automation-anywhere">
    <a class="lw-course-card--stretched-link" href="/course?courseid=automacao-robotica-de-processos-com-automation-anywhere">Automação Robótica de Processos (RPA) com Automation Anywhere</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/c44306b8b61655200c631c6ee386dbf6.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">88 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        RPA Automation Anywhere Automação de Processos
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">88 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Automação Robótica de Processos (RPA) com Automation Anywhere</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.230</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=automacao-robotica-de-processos-com-automation-anywhere" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=automacao-robotica-de-processos-com-uipath">
    <a class="lw-course-card--stretched-link" href="/course?courseid=automacao-robotica-de-processos-com-uipath">Automação Robótica de Processos (RPA) com UiPath</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f08801c5e36968d8e1fa85efd116a939.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">88 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        RPA Automação de Processos UiPath
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">88 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Automação Robótica de Processos (RPA) com UiPath</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.250</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=automacao-robotica-de-processos-com-uipath" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=automacao-de-processos-e-engenharia-de-dados-com-python-excel-ia">
    <a class="lw-course-card--stretched-link" href="/course?courseid=automacao-de-processos-e-engenharia-de-dados-com-python-excel-ia">Automação de Processos e Engenharia de Dados com Python, Excel e IA</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/a36de23038673b7b1db3243945e1af98.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">100 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Linguagem Python Microsoft Excel Engenharia de Dados Automação de Processos Inteligência Artificial
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">100 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Automação de Processos e Engenharia de Dados com Python, Excel e IA</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.550</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=automacao-de-processos-e-engenharia-de-dados-com-python-excel-ia" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=automacao-de-workflows-com-microsoft-power-automate">
    <a class="lw-course-card--stretched-link" href="/course?courseid=automacao-de-workflows-com-microsoft-power-automate">Automação de Workflows com Microsoft Power Automate</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/c49344a2e61a686804260f38995818a5.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">84 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Power Automate Power BI CoPilot Microsoft SQL Server RPA Automação de Processos
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">84 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Automação de Workflows com Microsoft Power Automate</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.400</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=automacao-de-workflows-com-microsoft-power-automate" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=business-analytics-e-machine-learning-para-projetos-de-data-science">
    <a class="lw-course-card--stretched-link" href="/course?courseid=business-analytics-e-machine-learning-para-projetos-de-data-science">Business Analytics e Machine Learning Para Projetos de Data Science</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/8699d8ca00389b6483d0acbd26c7939e.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">144 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Machine Learning Business Analytics Business Data Science
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">144 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Business Analytics e Machine Learning Para Projetos de Data Science</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.590</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=business-analytics-e-machine-learning-para-projetos-de-data-science" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=cloud-computing-data-science">
    <a class="lw-course-card--stretched-link" href="/course?courseid=cloud-computing-data-science">Cloud Computing Data Science (com Amazon SageMaker e Microsoft Fabric)</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/86a3d2b0bd50f43a89b6ef7b28b7e6db.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">84 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Cloud Computing Amazon Web Services (AWS) Amazon SageMaker Microsoft Fabric Machine Learning
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">84 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Cloud Computing Data Science (com Amazon SageMaker e Microsoft Fabric)</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.390</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=cloud-computing-data-science" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=data-science-para-analise-multivariada-de-dados">
    <a class="lw-course-card--stretched-link" href="/course?courseid=data-science-para-analise-multivariada-de-dados">Data Science Para Análise Multivariada de Dados</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/c09489b823136c910fe836b427172e6c.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">80 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Data Science Análise Multivariada Análise de Cluster Análise de Componentes Principais (PCA) Análise Fatorial XGBoost
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">80 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Data Science Para Análise Multivariada de Dados</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.399</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=data-science-para-analise-multivariada-de-dados" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=deep-learning-para-aplicacoes-de-inteligencia-artificial-com-python-e-c">
    <a class="lw-course-card--stretched-link" href="/course?courseid=deep-learning-para-aplicacoes-de-inteligencia-artificial-com-python-e-c">Deep Learning Para Aplicações de Inteligência Artificial com Python e C++</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/8b65fb62f8f44fe1c96117abd94d3c91.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">96 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Inteligência Artificial ChatGPT Linguagem C++ Linguagem Python PyTorch TensorFlow Transformers Visão Computacional Processamento de Linguagem Natural Séries Temporais CoPilot
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">96 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Deep Learning Para Aplicações de Inteligência Artificial com Python e C++</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.740</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=deep-learning-para-aplicacoes-de-inteligencia-artificial-com-python-e-c" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=desenvolvimento-e-deploy-de-modelos-de-machine-learning">
    <a class="lw-course-card--stretched-link" href="/course?courseid=desenvolvimento-e-deploy-de-modelos-de-machine-learning">Desenvolvimento e Deploy de Modelos de Machine Learning</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/1fbffa68fb44c1b9383b52d5f7196b70.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">100 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Deploy de Modelos Machine Learning
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">100 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Desenvolvimento e Deploy de Modelos de Machine Learning</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.680</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=desenvolvimento-e-deploy-de-modelos-de-machine-learning" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=design-e-administracao-de-cloud-computing-com-aws">
    <a class="lw-course-card--stretched-link" href="/course?courseid=design-e-administracao-de-cloud-computing-com-aws">Design e Administração de Cloud Computing AWS</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/62a0ebf1f322ef32e850157045382829.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">72 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Cloud Computing Amazon Web Services (AWS) AWS SageMaker
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">72 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Design e Administração de Cloud Computing AWS</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/2da6cb59b3bb3ef4370553b40cf14575.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Equipe DSA</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.250</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=design-e-administracao-de-cloud-computing-com-aws" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=engenharia-financeira-com-inteligencia-artificial">
    <a class="lw-course-card--stretched-link" href="/course?courseid=engenharia-financeira-com-inteligencia-artificial">Engenharia Financeira com Inteligência Artificial</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/d4f4f6723570a275c43c532c0f724fd4.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">96 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Engenharia Financeira Inteligência Artificial Deep Learning PyTorch TensorFlow Linguagem Python Reinforcement Learning
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">96 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Engenharia Financeira com Inteligência Artificial</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.800</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=engenharia-financeira-com-inteligencia-artificial" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=engenharia-de-dados-com-airbyte-dbt-e-sql">
    <a class="lw-course-card--stretched-link" href="/course?courseid=engenharia-de-dados-com-airbyte-dbt-e-sql">Engenharia de Dados com Airbyte, DBT e SQL</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/90a7b80de8079dfc16363f77148c3f6e.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">96 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Airbyte DBT Linguagem SQL Engenharia de Dados Processo ETL
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">96 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Engenharia de Dados com Airbyte, DBT e SQL</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.540</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=engenharia-de-dados-com-airbyte-dbt-e-sql" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=engenharia-de-software-para-machine-learning">
    <a class="lw-course-card--stretched-link" href="/course?courseid=engenharia-de-software-para-machine-learning">Engenharia de Software Para Machine Learning</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/52d47aa29f0880daf19e578f719b99e4.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">64 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Inteligência Artificial Machine Learning Engenharia de Software
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">64 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Engenharia de Software Para Machine Learning</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$980</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=engenharia-de-software-para-machine-learning" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=ia-generativa-e-llms-para-processamento-de-linguagem-natural">
    <a class="lw-course-card--stretched-link" href="/course?courseid=ia-generativa-e-llms-para-processamento-de-linguagem-natural">IA Generativa e LLMs Para Processamento de Linguagem Natural</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/2571a333ceda5336e0b3921266c4094b.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">96 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Inteligência Artificial Large Language Models (LLMs) Processamento de Linguagem Natural
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">96 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">IA Generativa e LLMs Para Processamento de Linguagem Natural</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$2.040</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=ia-generativa-e-llms-para-processamento-de-linguagem-natural" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=ia-generativa-e-llms-para-a-area-de-direito">
    <a class="lw-course-card--stretched-link" href="/course?courseid=ia-generativa-e-llms-para-a-area-de-direito">IA Generativa e LLMs Para a Área de Direito</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/b9bf0f5ccab2a533ec8c915260dc471a.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">96 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Inteligência Artificial Processamento de Linguagem Natural Large Language Models (LLMs) IA Generativa
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">96 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">IA Generativa e LLMs Para a Área de Direito</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$2.100</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=ia-generativa-e-llms-para-a-area-de-direito" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=infraestrutura-como-codigo-com-terraform-aws-azure-e-databricks">
    <a class="lw-course-card--stretched-link" href="/course?courseid=infraestrutura-como-codigo-com-terraform-aws-azure-e-databricks">Infraestrutura Como Código com Terraform, AWS, Azure e Databricks</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/b61743bd74aa7e176c9d9fc2d50243fe.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">72 hs</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Cloud Computing Terraform Amazon Web Services (AWS) Microsoft Azure Databricks Infraestrutura Como Código (IaC) Docker Kubernetes Apache Flink
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">72 hs</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Infraestrutura Como Código com Terraform, AWS, Azure e Databricks</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Equipe DSA</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.410</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=infraestrutura-como-codigo-com-terraform-aws-azure-e-databricks" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=inteligencia-artificial-para-analise-de-imagens-medicas">
    <a class="lw-course-card--stretched-link" href="/course?courseid=inteligencia-artificial-para-analise-de-imagens-medicas">Inteligência Artificial Para Análise de Imagens Médicas</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/8dc815d4be01674ac8277dd435180ce4.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">96 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Visão Computacional Segmentação de Imagens IA Multimodal Inteligência Artificial
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">96 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Inteligência Artificial Para Análise de Imagens Médicas</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.600</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=inteligencia-artificial-para-analise-de-imagens-medicas" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=inteligencia-artificial-para-seguranca-cibernetica">
    <a class="lw-course-card--stretched-link" href="/course?courseid=inteligencia-artificial-para-seguranca-cibernetica">Inteligência Artificial Para Segurança Cibernética</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/dab227a43e8408f1f7d22c8ce52145a0.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">84 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Segurança Machine Learning Inteligência Artificial Cyber Security Linguagem Python Data Science Deep Learning
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">84 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Inteligência Artificial Para Segurança Cibernética</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Equipe DSA</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.449</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=inteligencia-artificial-para-seguranca-cibernetica" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=inteligencia-artificial-para-visao-computacional">
    <a class="lw-course-card--stretched-link" href="/course?courseid=inteligencia-artificial-para-visao-computacional">Inteligência Artificial Para Visão Computacional</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/db80857af54b4005a5843facab4e8ee9.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">96 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Inteligência Artificial Visão Computacional Deep Learning PyTorch TensorFlow Detecção de Objetos Segmentação de Imagens
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">96 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Inteligência Artificial Para Visão Computacional</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.540</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=inteligencia-artificial-para-visao-computacional" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=lgpd-governanca-de-dados-e-gestao-de-metadados-1">
    <a class="lw-course-card--stretched-link" href="/course?courseid=lgpd-governanca-de-dados-e-gestao-de-metadados-1">LGPD - Governança de Dados e Gestão de Metadados</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/9c6768b46c67bc36d2bbca4baf82fb52.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">84 horas</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        LGPD Governança de Dados Gestão de Metadados
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">84 horas</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">LGPD - Governança de Dados e Gestão de Metadados</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/de601b3140f2cc3ef949248282fca563.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Matheus Passos </p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.540</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=lgpd-governanca-de-dados-e-gestao-de-metadados-1" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=mlops-e-ciclo-de-vida-de-modelos-de-machine-learning">
    <a class="lw-course-card--stretched-link" href="/course?courseid=mlops-e-ciclo-de-vida-de-modelos-de-machine-learning">MLOps e Ciclo de Vida de Modelos de Machine Learning</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/68b1b662cb34d0750787ce8170d5114f.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">100 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Inteligência Artificial Machine Learning MLOps
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">100 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">MLOps e Ciclo de Vida de Modelos de Machine Learning</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.600</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=mlops-e-ciclo-de-vida-de-modelos-de-machine-learning" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=machine-learning-para-aplicacoes-biomedicas">
    <a class="lw-course-card--stretched-link" href="/course?courseid=machine-learning-para-aplicacoes-biomedicas">Machine Learning Para Aplicações Biomédicas</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/9dd54d6db110d5ecd6c3eb3b8e072a25.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">80 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Machine Learning Biomedicina
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">80 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Machine Learning Para Aplicações Biomédicas</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.540</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=machine-learning-para-aplicacoes-biomedicas" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=matematica-e-estatistica-aplicada-para-data-science-machine-learning-e-ia">
    <a class="lw-course-card--stretched-link" href="/course?courseid=matematica-e-estatistica-aplicada-para-data-science-machine-learning-e-ia">Matemática e Estatística Aplicada Para Data Science, Machine Learning e IA</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/deaaca490097778cae7fca71a7d10454.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">84 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Data Science Matemática Análise Estatística Estatística
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">84 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Matemática e Estatística Aplicada Para Data Science, Machine Learning e IA</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.199</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=matematica-e-estatistica-aplicada-para-data-science-machine-learning-e-ia" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=microsoft-power-bi-para-business-intelligence-e-data-science">
    <a class="lw-course-card--stretched-link" href="/course?courseid=microsoft-power-bi-para-business-intelligence-e-data-science">Microsoft Power BI Para Business Intelligence e Data Science</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/bbaf6af9eae0170d188653e362b94f00.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">72 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Gratuito Fundamentos Power BI Data Science Business Business Intelligence
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">72 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Microsoft Power BI Para Business Intelligence e Data Science</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Equipe DSA</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                <strong>Gratuito</strong>
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=microsoft-power-bi-para-business-intelligence-e-data-science" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=modelagem-de-series-temporais-e-real-time-analytics-com-apache-spark-e-databricks">
    <a class="lw-course-card--stretched-link" href="/course?courseid=modelagem-de-series-temporais-e-real-time-analytics-com-apache-spark-e-databricks">Modelagem de Séries Temporais e Real-Time Analytics com Apache Spark e Databricks</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f2b46463cc5383b95e183b9e191c331a.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">96 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Forecasting Séries Temporais Análise Estatística Modelagem Preditiva
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">96 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Modelagem de Séries Temporais e Real-Time Analytics com Apache Spark e Databricks</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.399</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=modelagem-de-series-temporais-e-real-time-analytics-com-apache-spark-e-databricks" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=modelagem-e-analise-de-dados-com-power-bi">
    <a class="lw-course-card--stretched-link" href="/course?courseid=modelagem-e-analise-de-dados-com-power-bi">Modelagem e Análise de Dados com Power BI</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/fa4ed28d47b33b4df1f374d502c42ee9.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">96 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Modelagem de Dados Power BI Analytics Banco de Dados Business Intelligence
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">96 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Modelagem e Análise de Dados com Power BI</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.440</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=modelagem-e-analise-de-dados-com-power-bi" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=modelagem-implementacao-e-governanca-de-data-warehouses">
    <a class="lw-course-card--stretched-link" href="/course?courseid=modelagem-implementacao-e-governanca-de-data-warehouses">Modelagem, Implementação e Governança de Data Warehouses</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/fb87ba4cecba08404e026b43824ff0d3.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">80 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Linguagem SQL Data Warehouse Governança de Dados Amazon Redshift Amazon Web Services (AWS) Great Expectations
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">80 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Modelagem, Implementação e Governança de Data Warehouses</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.300</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=modelagem-implementacao-e-governanca-de-data-warehouses" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=orquestracao-de-fluxos-de-dados-com-apache-airflow">
    <a class="lw-course-card--stretched-link" href="/course?courseid=orquestracao-de-fluxos-de-dados-com-apache-airflow">Orquestração de Fluxos de Dados com Apache Airflow</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/4626039ec3377e19b37bc0ed858a3321.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">84 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Apache Airflow Orquestração de Dados Arquitetura de Dados Linguagem Python
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">84 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Orquestração de Fluxos de Dados com Apache Airflow</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.430</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=orquestracao-de-fluxos-de-dados-com-apache-airflow" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=pipelines-de-analise-e-engenharia-de-dados-com-google-bigquery">
    <a class="lw-course-card--stretched-link" href="/course?courseid=pipelines-de-analise-e-engenharia-de-dados-com-google-bigquery">Pipelines de Análise e Engenharia de Dados com Google BigQuery</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/3edb3eafa2fb9462d8b45d8dd03d4082.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">86 hs</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Cloud Computing Banco de Dados Banco de Dados Relacional Modelagem de Dados Linguagem SQL Google BigQuery Pipelines de Dados
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">86 hs</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Pipelines de Análise e Engenharia de Dados com Google BigQuery</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Equipe DSA</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.500</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=pipelines-de-analise-e-engenharia-de-dados-com-google-bigquery" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=pipelines-de-ci-cd-para-operacoes-de-machine-learning-e-ia">
    <a class="lw-course-card--stretched-link" href="/course?courseid=pipelines-de-ci-cd-para-operacoes-de-machine-learning-e-ia">Pipelines de CI/CD Para Operações de Machine Learning e IA</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/927a2aea0dbcd9843d911c83980c2de2.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">100 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Inteligência Artificial Machine Learning Pipelines de CI/CD Jenkins Terraform
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">100 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Pipelines de CI/CD Para Operações de Machine Learning e IA</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.870</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=pipelines-de-ci-cd-para-operacoes-de-machine-learning-e-ia" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=pipelines-de-etl-e-machine-learning-com-apache-spark">
    <a class="lw-course-card--stretched-link" href="/course?courseid=pipelines-de-etl-e-machine-learning-com-apache-spark">Pipelines de ETL e Machine Learning com Apache Spark</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/c1f15b541b09c927bd33cd70f7523dd8.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">84 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Linguagem SQL Analytics Inteligência Artificial Machine Learning Apache Spark Pipelines de Dados Arquitetura de Dados Processo ETL
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">84 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Pipelines de ETL e Machine Learning com Apache Spark</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.349</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=pipelines-de-etl-e-machine-learning-com-apache-spark" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=power-bi-avancado-para-analise-de-dados-com-dax">
    <a class="lw-course-card--stretched-link" href="/course?courseid=power-bi-avancado-para-analise-de-dados-com-dax">Power BI Avançado para Análise de Dados com DAX</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/ae6f862883851d551f0cb9bc5fae7a53.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">70 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Power BI Expressões DAX
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">70 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Power BI Avançado para Análise de Dados com DAX</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Equipe DSA</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.040</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=power-bi-avancado-para-analise-de-dados-com-dax" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=projeto-e-implementacao-de-plataforma-de-dados-com-snowflake">
    <a class="lw-course-card--stretched-link" href="/course?courseid=projeto-e-implementacao-de-plataforma-de-dados-com-snowflake">Projeto e Implementação de Plataforma de Dados com Snowflake</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/1d538b27d3370abfff9eebe0e70eafbf.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">96 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Linguagem SQL Banco de Dados Relacional Banco de Dados Analytics Snowflake Cloud Computing Arquitetura de Dados Plataforma de Dados
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">96 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Projeto e Implementação de Plataforma de Dados com Snowflake</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.840</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=projeto-e-implementacao-de-plataforma-de-dados-com-snowflake" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=projetos-de-analise-de-dados-com-linguagem-python">
    <a class="lw-course-card--stretched-link" href="/course?courseid=projetos-de-analise-de-dados-com-linguagem-python">Projetos de Análise de Dados com Linguagem Python</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/2bda70c4b18b46c695c03983f90272d0.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">82 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Linguagem Python Analytics Portfólio de Projetos
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">82 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Projetos de Análise de Dados com Linguagem Python</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.420</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=projetos-de-analise-de-dados-com-linguagem-python" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=prompt-engineering-com-chatgpt-multimodal-para-analise-de-dados-e-data-science">
    <a class="lw-course-card--stretched-link" href="/course?courseid=prompt-engineering-com-chatgpt-multimodal-para-analise-de-dados-e-data-science">Prompt Engineering com ChatGPT Para Análise de Dados e Data Science</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/260713791b72a20bf378b8e4a8fa46f4.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">60 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        ChatGPT Data Science Analytics Prompt Engineering
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">60 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Prompt Engineering com ChatGPT Para Análise de Dados e Data Science</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/2da6cb59b3bb3ef4370553b40cf14575.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Equipe DSA</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.349</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=prompt-engineering-com-chatgpt-multimodal-para-analise-de-dados-e-data-science" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=pyspark-e-apache-kafka-para-processamento-de-dados-em-batch-e-streaming">
    <a class="lw-course-card--stretched-link" href="/course?courseid=pyspark-e-apache-kafka-para-processamento-de-dados-em-batch-e-streaming">PySpark e Apache Kafka Para Processamento de Dados em Batch e Streaming</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/9e471cd398ca2c8640455cd6276555bf.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">90 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Apache Kafka Apache Spark PySpark Processo ETL
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">90 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">PySpark e Apache Kafka Para Processamento de Dados em Batch e Streaming</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.400</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=pyspark-e-apache-kafka-para-processamento-de-dados-em-batch-e-streaming" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=r-fundamentos-para-anlise-de-dados">
    <a class="lw-course-card--stretched-link" href="/course?courseid=r-fundamentos-para-anlise-de-dados">R Fundamentos Para Análise de Dados</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/07d25985dfe507bc63576380d4de2d58.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">40 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Analytics Linguagem R
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">40 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">R Fundamentos Para Análise de Dados</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/2da6cb59b3bb3ef4370553b40cf14575.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Equipe DSA</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$565</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=r-fundamentos-para-anlise-de-dados" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=sql-para-analise-de-dados-e-data-science">
    <a class="lw-course-card--stretched-link" href="/course?courseid=sql-para-analise-de-dados-e-data-science">SQL Para Análise de Dados e Data Science</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/ea3636148dc286bd92d273f11151da92.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">96 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Linguagem SQL Data Science Banco de Dados Relacional Banco de Dados Analytics Inteligência Artificial ChatGPT
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">96 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">SQL Para Análise de Dados e Data Science</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$1.400</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=sql-para-analise-de-dados-e-data-science" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			
				

				
				<div class="col lw-card-mb span_3_of_12 span_3_of_12-tl span_4_of_12-tp span_6_of_12-sl span_12_of_12-sp no-padding learnworlds-align-center flex-item fg-0 lw-course-card lw-course-card7 va-sb flexible" tabindex="0" data-href="/course?courseid=storytelling-dashboards-e-tecnicas-de-apresentacao-para-cientistas-de-dados">
    <a class="lw-course-card--stretched-link" href="/course?courseid=storytelling-dashboards-e-tecnicas-de-apresentacao-para-cientistas-de-dados">Storytelling, Dashboards e Técnicas de Apresentação Para Cientistas de Dados</a>
        <div class="learnworlds-image no-margin-bottom learnworlds-bg-default stretched-bg learnworlds-framed-image learnworlds-element rectangle learnworlds-frame-size-full" style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f307a70e7235def93d57add2a0f04b88.png?client_id=5806214e5e4cdefeed8b4567&amp;width=400&amp;height=0');">

            <!-- overlay gia enrollment closed / coming soon -->
            

            

            <div class="lw-tags absolute tl">
                
                    
                        
                    
                

            </div>

        </div>


        <div class="lw-body-bg flex-item va-sb fg-1 lw-padding-small learnworlds-element">

            <div class="flex-item fg-1 va-sb">
                <!--<p class="lw-brand-text learnworlds-overline-text learnworlds-letter-casing-uppercase learnworlds-element">72 h</p>-->

                <!--
                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20">
                    
                        Storytelling Técnicas de Apresentação Dashboards Visualização de Dados
                    
                </p>
                -->

                <div class="lw-card-top">
                    <p class="lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom" data-node-type="text" data-magic="label">72 h</p>

                    <h3 class="learnworlds-heading3 learnworlds-element learnworlds-heading3-small no-margin-top">Storytelling, Dashboards e Técnicas de Apresentação Para Cientistas de Dados</h3>

                </div>

                <div class="lw-interior-mt">

                    <!--
                    
                        <div class="lw-card-author lw-cols one-row one-row-tl one-row-tp one-row-sl one-row-sp align-items-center">
                            <div class="col fsh-0 no-padding span_2_of_12 span_2_of_12-tl span_2_of_12-tp span_2_of_12-sl span_2_of_12-sp">
                                <div class="learnworlds-image learnworlds-bg-default circle stretched-bg learnworlds-framed-image learnworlds-element learnworlds-frame-size-full"   style="background-image:url('https://api.sa-br1.learnworlds.com/imagefile/https://lwfiles000.mycourse.app/datascienceacademy-public/f5904fbd21fa7766fafbe89d9d428121.png?client_id=5806214e5e4cdefeed8b4567&width=500&height=0');" ></div>
                            </div>
                            <div class="col no-padding">
                                <p class="learnworlds-main-text learnworlds-main-text-small learnworlds-element lw-text-color-fadeout20 weglot-exclude">Data Science Academy</p>
                            </div>
                        </div>
                    
                    -->

                    

                    
                        <div class="lw-course-card-price learnworlds-main-text learnworlds-element learnworlds-main-text-small learnworlds-align-center-tp learnworlds-align-center-sl learnworlds-align-center-sp">
                            <!--
                            
                            -->

                            
                                
                                    
                                        <span class="weglot-exclude">
                                            <strong>R$890</strong>
                                        </span>
                                    
                                
                            
                        </div>
                    
                    <div class="learnworlds-button-wrapper lw-content-block learnworlds-element">
                        <a href="/course?courseid=storytelling-dashboards-e-tecnicas-de-apresentacao-para-cientistas-de-dados" class="no-margin-top full-width learnworlds-button  learnworlds-button-small   learnworlds-button-solid-accent1  learnworlds-element">
                            <span>Inscreva-se </span>
                        </a>
                    </div>
                </div>

            </div>

        </div>


</div>

			

		

		</div>
'''
classe_curso = "lw-course-card--stretched-link"
classe_preco = 'lw-course-card-price'
classe_promocional = "v-middle weglot-exclude"
classe_ch = "lw-brand-text learnworlds-overline-text learnworlds-element no-margin-bottom"

