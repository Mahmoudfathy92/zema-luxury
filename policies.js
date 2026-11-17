/* Customer policies: based on Egyptian CPA guidance, reviewed 3 November 2026. */
const baseRenderPolicy=renderPolicy;
renderPolicy=function(view){const ar=state.lang==='ar';if(!['returns','payment'].includes(view))return baseRenderPolicy(view);const returns=ar?[
['الاستبدال والاسترجاع','نريد أن تكوني راضية عن اختياركِ من زيما. يمكنكِ طلب استبدال مشترياتكِ أو ردها خلال 14 يومًا تبدأ من استلامها، دون الحاجة إلى ذكر سبب، مع مراعاة الاستثناءات القانونية.'],
['حالة القطعة','عند تغيير الرأي، يجب أن تبقى القطعة بحالتها وقت البيع، دون تلف أو تغير بسبب الاستخدام. يُرجى الاحتفاظ بملحقاتها وتغليفها حيثما أمكن. هذا الشرط لا يلغي حقوقكِ إذا كانت القطعة معيبة.'],
['عيب أو منتج غير مطابق','إذا ظهر عيب خلال 30 يومًا من الاستلام، يمكنكِ طلب الاستبدال أو استرداد القيمة دون تكلفة إضافية. نلتزم بمعالجة طلب رد السلعة المعيبة أو استبدالها خلال أسبوع من التواصل معنا. وإذا وصلتكِ قطعة مختلفة عن طلبكِ، تواصلي معنا لتصحيح الأمر دون تحميلكِ تكلفته.'],
['تكلفة الشحن واسترداد المبلغ','تتحمل زيما تكاليف الإرجاع أو الاستبدال عند ممارسة الحقوق المقررة قانونًا، دون رسوم إدارية. تُرد القيمة بطريقة الدفع الأصلية، ويمكن الاتفاق معكِ على وسيلة أخرى مناسبة دون فرض رصيد متجر بدلًا من المال.'],
['تقديم الطلب','تواصلي مع زيما برقم الطلب وحددي القطعة وما إذا كنتِ تريدين الاستبدال أو الاسترجاع. في حالة العيب، يمكن إرفاق صور لتسهيل المراجعة دون اعتبارها شرطًا لإثبات الحق. سننسق معكِ استلام القطعة وطريقة رد القيمة.'],
['التخفيضات وحقوقكِ','تسري الحقوق القانونية أيضًا على قطع التخفيضات. الاستثناءات القانونية، ومنها المنتجات المصنوعة بمواصفات خاصة مطابقة لطلبكِ، تُطبق فقط حيث تنطبق فعليًا. ولا تحد هذه السياسة من أي حق أو ضمان يمنحه القانون.']
]:[
['Returns & Exchanges','You may request an exchange or refund within 14 days of receiving your purchase, without giving a reason, subject to applicable legal exceptions.'],
['Condition of the piece','For a change-of-mind return, the piece must remain in its condition at sale without customer-caused damage or alteration. Please keep its accessories and packaging where possible. This does not restrict your rights for defective goods.'],
['Defective or incorrect items','You may request a replacement or refund for a defect within 30 days of receipt at no extra cost. We handle defective-item replacement or refund requests within one week of being contacted. If we sent the wrong item, contact us so we can correct it at our expense.'],
['Shipping and refunds','ZEMA covers return or exchange costs when you exercise your statutory rights, with no administration fee. Refunds use the original payment method; another suitable method may be agreed with you. Store credit is never imposed in place of a monetary refund.'],
['How to request a return','Contact ZEMA with your order reference, the item and your preferred resolution. Photos may help us review a defect but are not a prerequisite for your rights. We will coordinate collection and the refund with you.'],
['Sale items and legal rights','Statutory rights also apply to sale items. Legal exceptions, including correctly supplied custom-made items, apply only where relevant. Your other legal rights and guarantees remain unaffected.']];
const payment=ar?[
['الدفع عند الاستلام','تُدفع قيمة الطلب نقدًا عند استلامه. لا نطلب بيانات بطاقة بنكية لإتمام طلب الدفع عند الاستلام.'],
['الإجمالي قبل الشحن','يعرض الطلب قيمة المنتجات والشحن والإجمالي. إذا كان سعر الشحن غير محدد، سنؤكده معكِ ونحصل على موافقتكِ على الإجمالي قبل إتمام الطلب وإرساله. رسالة استلام الطلب لا تعني تأكيد شحنه.'],
['تأكيد بيانات التوصيل','يرجى إدخال رقم هاتف وعنوان صحيحين لتنسيق التسليم. أي رسوم إضافية تُوضح ويُتفق عليها قبل الشحن؛ لا تُضاف رسوم مخفية.'],
['فحص الطلب والاسترجاع','إمكانية فتح الطرد قبل الدفع تعتمد على خدمة شركة الشحن ولا نعد بها قبل تأكيدها. وتظل حقوق الاستبدال والاسترجاع قائمة بعد التسليم.']
]:[
['Cash on Delivery','Pay for your order in cash when it arrives. Card details are not required for cash-on-delivery orders.'],
['Your final amount','Your order shows the product amount, shipping and total. If shipping is not priced yet, we will obtain your agreement to the final amount before finalizing and dispatching the order. A receipt email acknowledges your request; it does not confirm dispatch.'],
['Delivery details','Provide a correct phone number and address so delivery can be arranged. Any additional charge must be disclosed and agreed before dispatch; there are no hidden charges.'],
['Inspection and returns','Opening the parcel before payment depends on the courier service and is not promised unless confirmed. Your return and exchange rights continue after delivery.']];
const rows=view==='returns'?returns:payment;return `<section class="shell section-py policy" dir="${ar?'rtl':'ltr'}"><span class="micro-label">${ar?'خدمة العملاء':'CLIENT SERVICES'}</span><h1>${rows[0][0]}</h1><p>${rows[0][1]}</p>${rows.slice(1).map(([title,text])=>`<h2>${title}</h2><p>${text}</p>`).join('')}<p><a href="#${view==='returns'?'payment':'returns'}">${ar?(view==='returns'?'الدفع عند الاستلام':'الاستبدال والاسترجاع'):(view==='returns'?'Cash on Delivery':'Returns & Exchanges')} →</a></p></section>`;};
if(['returns','payment'].includes(state.currentView))renderView();
